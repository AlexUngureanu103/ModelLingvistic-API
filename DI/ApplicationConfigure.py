from injector import Binder

from Repositories.TranslationRepository import TranslationRepository
from Repositories.UserRepository import UserRepository
from Services.AccountService import AccountService


def configure(binder: Binder) -> None:
    binder.bind(TranslationRepository, to=TranslationRepository)
    binder.bind(UserRepository, to=UserRepository)
    binder.bind(AccountService, to=AccountService)
