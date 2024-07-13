#!/usr/bin/env python3
"""
    Auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Stub method"""
        return False

    def authorization_header(self, request=None) -> str:
        """Stub method"""
        return

    def current_user(self, request=None) -> TypeVar('User'):
        """Stub method"""
        return
