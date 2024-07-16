#!/usr/bin/env python3
"""
    Authentication module for SessionAuth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """CReate a Session id for a user"""
        if user_id is None or type(user_id) != str:
            return

        session_id = str(uuid.uuid4())
        type(self).user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get a user id associated with session id"""
        if session_id is None or type(session_id) != str:
            return

        return type(self).user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""
        cookie = self.session_cookie(request)
        if cookie:
            user_id = self.user_id_for_session_id(cookie)
            if user_id:
                return User.get(user_id)
