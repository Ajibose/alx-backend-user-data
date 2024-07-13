#!/usr/bin/env python3
"""
    Authentication module
"""
from models.user import User
from api.v1.auth.auth import Auth
from typing import TypeVar
import re
import base64


class BasicAuth(Auth):
    """Basic Autentication"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header"""
        if authorization_header is None or type(authorization_header) != str:
            return None

        if re.match(r'Basic ', authorization_header):
            match = re.fullmatch(r'Basic ([\w=]+)', authorization_header)
            if match:
                return match.group(1)

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a base64 string"""
        if type(base64_authorization_header) == str:
            try:
                data = base64.b64decode(base64_authorization_header)
            except Exception:
                pass
            else:
                return data.decode("utf-8")

        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Return thr user data from base64 decoded string"""
        if type(decoded_base64_authorization_header) == str:
            data_list = decoded_base64_authorization_header.split(':')
            if len(data_list) < 2:
                return None, None

            email, passwd = data_list
            return email, passwd

        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Find User instance based on his email and password"""
        if user_email is None or user_pwd is None:
            return None

        users = User.search({'email': user_email})

        if len(users) > 0:
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

        return None
