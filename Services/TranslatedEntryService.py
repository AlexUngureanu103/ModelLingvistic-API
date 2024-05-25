from Models.RequestStatus import RequestStatus
from Models.TranslatedEntry import CreateOrUpdateTranslatedEntry
from Repositories.TranslatedEntryRepository import TranslatedEntryRepository
from Repositories.UserRepository import UserRepository


class TranslatedEntryService:
    def __init__(self, translated_entry_repository: TranslatedEntryRepository, user_repository: UserRepository):
        self.user_repository = user_repository
        self.translated_entry_repository = translated_entry_repository
        self.request_status = RequestStatus()

    def _reset_request_status(self):
        self.request_status = RequestStatus()

    def get_translated_entry(self, entry_id):
        return self.translated_entry_repository.get_translated_entry(entry_id)

    def get_all_translated_entries(self):
        return self.translated_entry_repository.get_all_translated_entries()

    def get_all_translated_entries_by_user(self, user_id):
        return self.translated_entry_repository.get_all_translated_entries_by_user(user_id)

    def add_translated_entry(self, translated_entry: CreateOrUpdateTranslatedEntry):
        self._reset_request_status()
        if not self.user_repository.get_user(translated_entry.user_id):
            self.request_status.add_error("error", "User does not exist")
            return self.request_status

        self.translated_entry_repository.add_translated_entry(translated_entry)

        return self.request_status

    def update_translated_entry(self, entry_id: str, translated_entry: CreateOrUpdateTranslatedEntry):
        self._reset_request_status()
        if not self.translated_entry_repository.get_translated_entry(entry_id):
            self.request_status.add_error("error", "Entry does not exist")
            return self.request_status

        self.translated_entry_repository.update_translated_entry(entry_id, translated_entry)
        return self.request_status

    def delete_translated_entry(self, entry_id: str):
        self._reset_request_status()
        if not self.translated_entry_repository.get_translated_entry(entry_id):
            self.request_status.add_error("error", "Entry does not exist")
            return self.request_status

        self.translated_entry_repository.delete_translated_entry(entry_id)

        return self.request_status
