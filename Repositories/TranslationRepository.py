import uuid
from pymongo import MongoClient
from Models import Translation
from config import Environment, TranslationCollection


class TranslationRepository:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client[Environment]
        self.collection = self.db[TranslationCollection]

    def add_translation(self, translation: Translation):
        unique_id = str(uuid.uuid4())

        translation._id = unique_id

        result = self.collection.insert_one(translation.__dict__)
        return result.inserted_id

    def get_translation(self, translation_id) -> Translation:
        translation = self.collection.find_one({'_id': translation_id})
        return translation

    def update_translation(self, translation_id, translation: Translation):
        self.collection.update_one({'_id': translation_id}, {"$set": translation.__dict__})

    def delete_translation(self, translation_id):
        self.collection.delete_one({'_id': translation_id})
