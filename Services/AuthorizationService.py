import hashlib
import datetime
from functools import wraps
import jwt
from flask import request, jsonify

from config import SECRET_KEY, ALGORITHM


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            bearer, token = request.headers['Authorization'].split()
            if bearer != 'Bearer':
                return jsonify({'error': 'Invalid token format!'}), 401

        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            current_user = data['user_id']
        except:
            return jsonify({'error': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(hashed_password: str, user_password: str) -> bool:
    return hashed_password == hash_password(user_password)


def create_token(user_id: str) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
