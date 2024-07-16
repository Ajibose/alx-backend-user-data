#!/usr/bin/env python3
"""Session Authentication views
"""
from api.v1.views import app_views
from flask import request, jsonify
from os import getenv
from models.user import User
from models.base import DATA


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """Session login"""
    email = request.form.get('email')
    passwd = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not passwd:
        return jsonify({"error": "password missing"}), 400

    if 'User' not in DATA:
        return jsonify({"error": "no user found for this email"}), 404

    users = User.search({'email': email})

    if users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(passwd):
            from api.v1.app import auth
            cookie = getenv('SESSION_NAME')
            sid = auth.create_session(user.id)
            resp = jsonify(user.to_json())
            resp.set_cookie(cookie, sid)
            return resp

    return jsonify({"error": "wrong password"}), 400
