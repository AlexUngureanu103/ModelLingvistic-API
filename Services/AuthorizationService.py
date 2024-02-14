import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password( hashed_password: str, user_password: str) -> bool:
    return hashed_password == hash_password(user_password)
