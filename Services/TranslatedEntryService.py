from Models.RequestStatus import RequestStatus
from Models.TranslationEntry import CreateOrUpdateTranslationEntry
from Repositories.HistoryTranslationEntryRepository import HistoryTranslationEntryRepository
from Repositories.UserRepository import UserRepository


class TranslatedEntryService:
    def __init__(self, history_translation_entry_repository: HistoryTranslationEntryRepository,
                 user_repository: UserRepository):
        self.user_repository = user_repository
        self.history_translation_entry_repository = history_translation_entry_repository
        self.request_status = RequestStatus()

    def _reset_request_status(self):
        self.request_status = RequestStatus()

    def get_all_translated_entries(self):
        return self.history_translation_entry_repository.get_all_translated_entries()

    def get_all_translated_entries_by_user(self, user_id):
        return self.history_translation_entry_repository.get_all_translated_entries_by_user(user_id)

    def add_translated_entry(self, translated_entry: CreateOrUpdateTranslationEntry):
        self._reset_request_status()
        if not self.user_repository.get_user(translated_entry.user_id):
            self.request_status.add_error("error", "User does not exist")
            return self.request_status

        self.history_translation_entry_repository.add_translated_entry(translated_entry)

        return self.request_status

    def update_translated_entry(self, user_id: str, translated_entries: list):
        self._reset_request_status()

        db_entries = self.history_translation_entry_repository.get_all_translated_entries_by_user(user_id)

        for entry in db_entries:
            self.history_translation_entry_repository.delete_translated_entry(entry["_id"])

        for entry in translated_entries:
            self.history_translation_entry_repository.add_translated_entry(entry)

        return self.request_status

    def delete_translated_entry(self, user_id: str, entry_id: str):
        self._reset_request_status()

        db_entry = self.history_translation_entry_repository.get_translated_entry_by_id(entry_id)

        if db_entry and db_entry["user_id"] == user_id:
            self.history_translation_entry_repository.delete_translated_entry(entry_id)
        else:
            self.request_status.add_error("error", "Entry not found")

        return self.request_status
