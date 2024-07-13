#!/usr/bin/env python3
"""
    Authentication module
"""
from api.v1.auth.auth import Auth
import re


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
