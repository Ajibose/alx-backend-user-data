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
        if path is None or not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        for excluded in excluded_paths:
            if excluded.endswith("*"):
                truthy = path.startswith(excluded[0:-1])
            else:
                truthy = path == excluded
            if truthy:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Return the request authorization header"""
        if request is None:
            return

        header = request.headers.get('Authorization')

        return header

    def session_cookie(self, request=None):
        """Return a cookie from a request"""
        if request is None:
            return

        from os import getenv
        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
