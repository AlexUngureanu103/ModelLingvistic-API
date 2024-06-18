from flask import Blueprint, request, jsonify

from Models.TranslatedEntry import CreateOrUpdateTranslatedEntry
from Repositories.UserRepository import UserRepository
from Repositories.TranslatedEntryRepository import TranslatedEntryRepository
from Services.AuthorizationService import token_required
from Services.TranslatedEntryService import TranslatedEntryService

translated_entry_controller = Blueprint('translated_entry_controller', __name__)

translated_entry_repository = TranslatedEntryRepository()
user_repository = UserRepository()
translated_entry_service = TranslatedEntryService(translated_entry_repository, user_repository)


@translated_entry_controller.route('/translated-entry', methods=['POST'])
@token_required
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

    status = translated_entry_service.add_translated_entry(translated_entry)

    if status.is_empty():
        return jsonify(translated_entry.to_dict())
    else:
        return jsonify(status.errors), 400


@translated_entry_controller.route('/translated-entry', methods=['DELETE'])
@token_required
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
    status = translated_entry_service.delete_translated_entry(entry_id)

    if status.is_empty():
        return jsonify("Translated entry deleted successfully")
    else:
        return jsonify(status.errors), 400


@translated_entry_controller.route('/translated-entry', methods=['PUT'])
@token_required
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

    status = translated_entry_service.update_translated_entry(translated_entry_data['entry_id'], translated_entry)

    if status.is_empty():
        return jsonify("Translated entry updated successfully")
    else:
        return jsonify(status.errors), 400


@translated_entry_controller.route('/translated-entry', methods=['GET'])
@token_required
def get_all_translated_entries_by_user(current_user: str):
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
    translated_entries = translated_entry_service.get_all_translated_entries_by_user(current_user)

    return jsonify(translated_entries)


@translated_entry_controller.route('/translated-entry/single/<entry_id>', methods=['GET'])
@token_required
def get_translated_entry(entry_id: str):
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
    translated_entry = translated_entry_service.get_translated_entry(entry_id)

    return jsonify(translated_entry)
