import uuid
from pymongo import MongoClient
from Models import Translation
from config import Environment, TranslationCollection, DB_CONNECTION_STRING


class TranslationRepository:
    def __init__(self):
        self.client = MongoClient(DB_CONNECTION_STRING)
        self.db = self.client[Environment]
        self.collection = self.db[TranslationCollection]

    def add_translation(self, translation: Translation):
        unique_id = str(uuid.uuid4())

        translation._id = unique_id

        result = self.collection.insert_one(translation.__dict__)
        return result.inserted_id

    def get_translation(self, translation_id: str) -> Translation:
        translation = self.collection.find_one({'_id': translation_id})
        return translation

    def update_translation(self, translation_id: str, translation: Translation):
        self.collection.update_one({'_id': translation_id}, {"$set": translation.__dict__})

    def delete_translation(self, translation_id: str):
        self.collection.delete_one({'_id': translation_id})
