from Models.RequestStatus import RequestStatus
from Models.TranslationEntry import CreateOrUpdateTranslationEntry
from Repositories import FavoriteTranslationEntryRepository
from Repositories.UserRepository import UserRepository


class FavoriteTranslationEntryService:
    def __init__(self, favorite_translation_entry_repository: FavoriteTranslationEntryRepository,
                 user_repository: UserRepository):
        self.user_repository = user_repository
        self.favorite_translation_entry_repository = favorite_translation_entry_repository
        self.request_status = RequestStatus()

    def _reset_request_status(self):
        self.request_status = RequestStatus()

    def get_all_translated_entries(self):
        return self.favorite_translation_entry_repository.get_all_translated_entries()

    def get_all_translated_entries_by_user(self, user_id):
        return self.favorite_translation_entry_repository.get_all_translated_entries_by_user(user_id)

    def add_translated_entry(self, translated_entry: CreateOrUpdateTranslationEntry):
        self._reset_request_status()
        if not self.user_repository.get_user(translated_entry.user_id):
            self.request_status.add_error("error", "User does not exist")
            return self.request_status

        self.favorite_translation_entry_repository.add_translated_entry(translated_entry)

        return self.request_status

    def update_translated_entry(self, user_id: str, translated_entries: list):
        self._reset_request_status()

        db_entries = self.favorite_translation_entry_repository.get_all_translated_entries_by_user(user_id)

        for entry in db_entries:
            self.favorite_translation_entry_repository.delete_translated_entry(entry["_id"])

        for entry in translated_entries:
            self.favorite_translation_entry_repository.add_translated_entry(entry)

        return self.request_status
