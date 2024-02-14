import uuid
from pymongo import MongoClient
from Models import User
from config import Environment, AccountCollection


class UserRepository:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client[Environment]  # replace with your database name
        self.collection = self.db[AccountCollection]  # replace with your collection name

    def create_user(self, user: User):
        unique_id = str(uuid.uuid4())

        user._id = unique_id

        result = self.collection.insert_one(user.__dict__)
        return result.inserted_id

    def get_user(self, user_id) -> User:
        user = self.collection.find_one({'_id': user_id})
        return user

    def get_user_by_email(self, email) -> User:
        user = self.collection.find_one({'email': email})
        return user

    def update_user(self, user_id, user: User):
        self.collection.update_one({'_id': user_id}, {"$set": user.__dict__})

    def delete_user(self, user_id):
        self.collection.delete_one({'_id': user_id})
