from flask import Blueprint, request, jsonify

from Models.User import CreateOrUpdateUser, User
from Repositories.UserRepository import UserRepository
from Services.AccountService import AccountService
from Services.AuthorizationService import token_required

user_controller = Blueprint('user_controller', __name__)

user_repository = UserRepository()
accountService = AccountService(user_repository)


@user_controller.route('/user/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    tags:
      - Account
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The email of the account.
        schema:
          type: object
          properties:
            email:
              type: string
              example: "test@example.com"
            password:
              type: string
              example: "password123"

    responses:
      200:
        description: Successful operation
    """
    user_data = request.json
    user = CreateOrUpdateUser(user_data['email'], user_data['password'])
    status = accountService.register(user)

    if status.is_empty():
        return jsonify(status.data)
    else:
        return jsonify(status.errors), 400


@user_controller.route('/user/login', methods=['POST'])
def login():
    """
    Login a user
    ---
    tags:
      - Account
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The email of the account.
        schema:
          type: object
          properties:
            email:
              type: string
              example: "test@example.com"
            password:
              type: string
              example: "password123"
    responses:
      200:
        description: Successful operation
    """
    user_data = request.json
    user = CreateOrUpdateUser(user_data['email'], user_data['password'])
    status = accountService.login(user)

    if status.is_empty():
        return jsonify(status.data)
    else:
        return jsonify(status.errors), 401


@user_controller.route('/user/delete', methods=['DELETE'])
@token_required
def delete(current_user: str):
    """
    Delete a user
    ---
    tags:
      - Account
    parameters:
      - name: user_id
        in: body
        required: true
        type: string
        description: The id of the account.
        schema:
          type: object
          properties:
            id:
              type: string
              id: "1234567890"

    responses:
      200:
        description: Successful operation
    """
    status = accountService.delete_account(current_user)

    if status.is_empty():
        return jsonify("User delete successfully")
    else:
        return jsonify(status.errors), 400


@user_controller.route('/user/update', methods=['PUT'])
@token_required
def update(current_user: str):
    """
    Update a user
    ---
    tags:
      - Account
    parameters:
      - name: body
        in: body
        required: true
        type: string
        description: The email of the account.
        schema:
          type: object
          properties:
            email:
              type: string
              example: "test@example.com"
            password:
              type: string
              example: "password123"
    responses:
      200:
        description: Successful operation
    """
    user_data = request.json
    user = User(current_user, email=user_data['email'], password=user_data['password'])
    status = accountService.update_account(current_user, user)

    if status.is_empty():
        return jsonify("User Update successfully")
    else:
        return jsonify(status.errors), 400
