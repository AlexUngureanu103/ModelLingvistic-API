class User:
    def __init__(self, _id: str, password: str, email: str):
        self.password = password
        self.email = email
        self._id = _id


class CreateOrUpdateUser:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self._id = None

    @property
    def id(self):
        return self._id
