from Models.RequestStatus import RequestStatus
from Models.User import User, CreateOrUpdateUser
from Repositories.UserRepository import UserRepository
from Services.AuthorizationService import hash_password, verify_password


class AccountService:
    def __init__(self, user_repository: UserRepository):
        self.userRepository = user_repository
        self.requestStatus = RequestStatus()

    def _reset_request_status(self):
        self.requestStatus = RequestStatus()

    def register(self, user: CreateOrUpdateUser):
        self._reset_request_status()
        if user.email == "" or user.password == "":
            self.requestStatus.add_error("error", "Email and password are required")
            return self.requestStatus

        if self.userRepository.get_user_by_email(user.email):
            self.requestStatus.add_error("error", "Email already exists")
            return self.requestStatus

        user.password = hash_password(user.password)
        self.userRepository.create_user(user)

        self.requestStatus.add_data("user_id", user._id)
        return self.requestStatus

    def delete_account(self, user_id):
        self._reset_request_status()
        if not self.userRepository.get_user(user_id):
            self.requestStatus.add_error("error", "User does not exist")
            return self.requestStatus

        self.userRepository.delete_user(user_id)
        return self.requestStatus

    def update_account(self, user_id, user: CreateOrUpdateUser):
        self._reset_request_status()
        if not self.userRepository.get_user(user_id):
            self.requestStatus.add_error("error", "User does not exist")
            return self.requestStatus

        if user.email == "" or user.password == "":
            self.requestStatus.add_error("error", "Email and password are required")
            return self.requestStatus

        if self.userRepository.get_user_by_email(user.email):
            self.requestStatus.add_error("error", "Email already exists")
            return self.requestStatus

        self.userRepository.update_user(user_id, user)
        return self.requestStatus

    def login(self, user: CreateOrUpdateUser):
        self._reset_request_status()
        if user.email == "" or user.password == "":
            self.requestStatus.add_error("error", "Email and password are required")
            return self.requestStatus

        user_from_db = self.userRepository.get_user_by_email(user.email)

        if user_from_db is None:
            self.requestStatus.add_error("error", "User does not exist")
            return self.requestStatus

        password_ok = verify_password(user_from_db["password"], user.password)
        if password_ok:
            self.requestStatus.add_data("user_id", user_from_db["_id"])
            return self.requestStatus

        self.requestStatus.add_error("error", "Password is incorrect")
        return self.requestStatus
