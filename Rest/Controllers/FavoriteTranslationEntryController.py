from flask import Blueprint, request, jsonify

from Models.TranslationEntry import CreateOrUpdateTranslationEntry, TranslationEntry
from Repositories.FavoriteTranslationEntryRepository import FavoriteTranslationEntryRepository
from Repositories.UserRepository import UserRepository
from Services.AuthorizationService import token_required
from Services.FavoriteTranslationEntryService import FavoriteTranslationEntryService

favorite_translation_entry_controller = Blueprint('favorite_translated_entry_controller', __name__)

favorite_translation_entry_repository = FavoriteTranslationEntryRepository()
user_repository = UserRepository()
favorite_translation_entry_service = FavoriteTranslationEntryService(favorite_translation_entry_repository,
                                                                     user_repository)


@favorite_translation_entry_controller.route('/favorite-translated-entry', methods=['POST'])
@token_required
def add_translated_entry(current_user: str):
    """
    Add a favorite translated entry
    ---
    tags:
      - Favorite
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The translated entry to add.
        schema:
          type: object
          properties:
            locale_id:
              type: integer
              example: 0
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
    translated_entry = CreateOrUpdateTranslationEntry(
        user_id=current_user,
        prompt_language=translated_entry_data['source_language'],
        translated_language=translated_entry_data['target_language'],
        prompt=translated_entry_data['prompt'],
        translated_prompt=translated_entry_data['translation'],
        locale_id=translated_entry_data['locale_id']
    )

    status = favorite_translation_entry_service.add_translated_entry(translated_entry)

    if status.is_empty():
        return jsonify(translated_entry.to_dict())
    else:
        return jsonify(status.errors), 400


@favorite_translation_entry_controller.route('/favorite-translated-entry', methods=['PUT'])
@token_required
def update_translated_entry(current_user: str):
    """
    Update favorite translated entries
    ---
    tags:
      - Favorite
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The translated entry to update.
        schema:
          type: array
          properties:
            locale_id:
              type: integer
              example: 0
            remote_id:
              type: string
              example: "1234567890"
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
    translated_entries_data = request.json

    translated_entries = []

    for translated_entry_data in translated_entries_data:
        # Create a TranslatedEntry object for each dictionary in the list
        translated_entry = TranslationEntry(
            user_id=current_user,
            prompt_language=translated_entry_data['source_language'],
            translated_language=translated_entry_data['target_language'],
            prompt=translated_entry_data['prompt'],
            translated_prompt=translated_entry_data['translation'],
            locale_id=translated_entry_data['locale_id'],
            _id=translated_entry_data['_id']
        )
        translated_entries.append(translated_entry)

    status = favorite_translation_entry_service.update_translated_entry(current_user, translated_entries)

    if status.is_empty():
        return jsonify("Translated entries updated successfully")
    else:
        return jsonify(status.errors), 400


@favorite_translation_entry_controller.route('/favorite-translated-entry', methods=['GET'])
@token_required
def get_all_translated_entries_by_user(current_user: str):
    """
    Get all favorite translated entries by user
    ---
    tags:
      - Favorite
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    translated_entries = favorite_translation_entry_service.get_all_translated_entries_by_user(current_user)

    return jsonify(translated_entries)
