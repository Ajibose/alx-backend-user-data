#!/usr/bin/env python3
"""
    Authentication module
"""
from api.v1.auth.auth import Auth
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

