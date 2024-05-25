import injector
from flask import Blueprint, request, jsonify

from DI.ApplicationConfigure import configure
from Models.TranslatedEntry import TranslatedEntry, CreateOrUpdateTranslatedEntry
from Models.User import CreateOrUpdateUser, User
from Repositories.UserRepository import UserRepository
from Repositories.TranslatedEntryRepository import TranslatedEntryRepository
from Services.TranslatedEntryService import TranslatedEntryService
from config import DB_CONNECTION_STRING

translated_entry_controller = Blueprint('translated_entry_controller', __name__)

translated_entry_repository = TranslatedEntryRepository()
user_repository = UserRepository()
tralated_entry_service = TranslatedEntryService(translated_entry_repository, user_repository)


@translated_entry_controller.route('/translated-entry', methods=['POST'])
def add_translated_entry():
    """
    Add a translated entry
    ---
    tags:
      - Translated Entry
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The translated entry to add.
        schema:
          type: object
          properties:
            user_id:
              type: string
              example: "user_id"
            source_language:
              type: string
              example: "English"
            target_language:
              type: string
              example: "Romanian"
            prompt:
              type: string
              example: "Translate this text."
            translation:
              type: string
              example: "Traduceti acest text."
    responses:
      200:
        description: Successful operation
    """
    translated_entry_data = request.json
    translated_entry = CreateOrUpdateTranslatedEntry(
        user_id=translated_entry_data['user_id'],
        prompt_language=translated_entry_data['source_language'],
        translated_language=translated_entry_data['target_language'],
        prompt=translated_entry_data['prompt'],
        translated_prompt=translated_entry_data['translation'])

    status = tralated_entry_service.add_translated_entry(translated_entry)

    if status.is_empty():
        return jsonify("Translated entry added successfully")
    else:
        return jsonify(status.errors), 400


@translated_entry_controller.route('/translated-entry', methods=['DELETE'])
def delete_translated_entry():
    """
    Delete a translated entry
    ---
    tags:
      - Translated Entry
    parameters:
      - name: entry_id
        in: body
        required: true
        type: string
        description: The id of the translated entry.
        schema:
          type: object
          properties:
            id:
              type: string
              example: "entry_id"
    responses:
      200:
        description: Successful operation
    """
    entry_id = request.json.get('id')
    status = tralated_entry_service.delete_translated_entry(entry_id)

    if status.is_empty():
        return jsonify("Translated entry deleted successfully")
    else:
        return jsonify(status.errors), 400


@translated_entry_controller.route('/translated-entry', methods=['PUT'])
def update_translated_entry():
    """
    Update a translated entry
    ---
    tags:
      - Translated Entry
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The translated entry to update.
        schema:
          type: object
          properties:
            entry_id:
              type: string
              example: "entry_id"
            user_id:
              type: string
              example: "user_id"
            source_language:
              type: string
              example: "English"
            target_language:
              type: string
              example: "Romanian"
            prompt:
              type: string
              example: "Translate this text."
            translation:
              type: string
              example: "Traduceti acest text."
    responses:
      200:
        description: Successful operation
    """
    translated_entry_data = request.json
    translated_entry = CreateOrUpdateTranslatedEntry(
        user_id=translated_entry_data['user_id'],
        prompt_language=translated_entry_data['source_language'],
        translated_language=translated_entry_data['target_language'],
        prompt=translated_entry_data['prompt'],
        translated_prompt=translated_entry_data['translation'])

    status = tralated_entry_service.update_translated_entry(translated_entry_data['entry_id'], translated_entry)

    if status.is_empty():
        return jsonify("Translated entry updated successfully")
    else:
        return jsonify(status.errors), 400


@translated_entry_controller.route('/translated-entry', methods=['GET'])
def get_all_translated_entries():
    """
    Get all translated entries
    ---
    tags:
      - Translated Entry
    responses:
      200:
        description: Successful operation
    """
    translated_entries = tralated_entry_service.get_all_translated_entries()

    return jsonify(translated_entries)


@translated_entry_controller.route('/translated-entry/<user_id>', methods=['GET'])
def get_all_translated_entries_by_user(user_id):
    """
    Get all translated entries by user
    ---
    tags:
      - Translated Entry
    parameters:
      - name: user_id
        in: path
        required: true
        type: string
        description: The id of the user.
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    translated_entries = tralated_entry_service.get_all_translated_entries_by_user(user_id)

    return jsonify(translated_entries)


@translated_entry_controller.route('/translated-entry/<entry_id>', methods=['GET'])
def get_translated_entry(entry_id):
    """
    Get a translated entry
    ---
    tags:
      - Translated Entry
    parameters:
      - name: user_id
        in: path
        required: true
        type: string
        description: The id of the user.
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    translated_entry = tralated_entry_service.get_translated_entry(entry_id)

    return jsonify(translated_entry)
