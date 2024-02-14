# from injector import Injector, inject, Module, provider, singleton
# from config import DB_CONNECTION_STRING
# from Repositoes.UserRepository import UserRepository
# from Services.AccountService import AccountService
#
#
# class AppModule(Module):
#     @singleton
#     @provider
#     def provide_user_repository(self) -> UserRepository:
#         return UserRepository(DB_CONNECTION_STRING)
#
#     @singleton
#     @provider
#     @inject
#     def provide_account_service(self, user_repository: UserRepository) -> AccountService:
#         return AccountService(user_repository)
#
#
# injector = Injector(AppModule())