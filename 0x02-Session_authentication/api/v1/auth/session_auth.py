#!/usr/bin/env python3
"""
    Authentication module for SessionAuth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """CReate a Session id for a user"""
        if user_id is None or type(user_id) != str:
            return

        session_id = uuid.uuid4()
        type(self).user_id_by_session_id[session_id] = user_id
        return session_id
