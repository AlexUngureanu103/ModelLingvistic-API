import uuid
from pymongo import MongoClient
from Models.TranslationEntry import TranslationEntry
from config import Environment, DB_CONNECTION_STRING, FavoriteTranslatedEntryCollection


class FavoriteTranslationEntryRepository:
    def __init__(self):
        self.client = MongoClient(DB_CONNECTION_STRING)
        self.db = self.client[Environment]
        self.collection = self.db[FavoriteTranslatedEntryCollection]

    def add_translated_entry(self, history_translated_entry: TranslationEntry):
        unique_id = str(uuid.uuid4())

        history_translated_entry._id = unique_id

        result = self.collection.insert_one(history_translated_entry.__dict__)
        return result.inserted_id

    def get_all_translated_entries(self):
        cursor = self.collection.find()
        translated_entries = [entry for entry in cursor]
        return translated_entries

    def get_all_translated_entries_by_user(self, user_id: str):
        cursor = self.collection.find({'user_id': user_id})
        translated_entries = [entry for entry in cursor]
        return translated_entries

    def get_translated_entry(self, entry_id: str):
        translated_entry = self.collection.find_one({'_id': entry_id})
        return translated_entry

    def update_translated_entry(self, entry_id: str, history_translated_entry: TranslationEntry):
        self.collection.update_one({'_id': entry_id}, {"$set": history_translated_entry.__dict__})

    def delete_translated_entry(self, translated_entry_id: str):
        self.collection.delete_one({'_id': translated_entry_id})
