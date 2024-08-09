#!/usr/bin/env python3
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database."""
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Authenticate user"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"{user.email} already exists")
        except NoResultFound:
            hashed_passwd = _hash_password(password)
            user = User(email=email, hashed_password=hashed_passwd)
            self._db._session.add(user)
            self._db._session.commit()
            return user
