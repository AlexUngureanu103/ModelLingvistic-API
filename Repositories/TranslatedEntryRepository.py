import uuid
from pymongo import MongoClient
from Models import Translation
from Models.TranslatedEntry import TranslatedEntry
from config import Environment, DB_CONNECTION_STRING, TranslatedEntryCollection


class TranslatedEntryRepository:
    def __init__(self):
        self.client = MongoClient(DB_CONNECTION_STRING)
        self.db = self.client[Environment]
        self.collection = self.db[TranslatedEntryCollection]

    def add_translated_entry(self, translated_entry: TranslatedEntry):
        unique_id = str(uuid.uuid4())

        translated_entry._id = unique_id

        result = self.collection.insert_one(translated_entry.__dict__)
        return result.inserted_id

    def get_all_translated_entries(self):
        cursor = self.collection.find()
        translated_entries = [entry for entry in cursor]
        return translated_entries

    def get_all_translated_entries_by_user(self, user_id: str):
        cursor = self.collection.find({'user_id': user_id})
        translated_entries = [entry for entry in cursor]
        return translated_entries

    def get_translated_entry(self, translated_entry_id: str):
        translated_entry = self.collection.find_one({'_id': translated_entry_id})
        return translated_entry

    def update_translated_entry(self, translated_entry_id: str, translated_entry: TranslatedEntry):
        self.collection.update_one({'_id': translated_entry_id}, {"$set": translated_entry.__dict__})

    def delete_translated_entry(self, translated_entry_id: str):
        self.collection.delete_one({'_id': translated_entry_id})
