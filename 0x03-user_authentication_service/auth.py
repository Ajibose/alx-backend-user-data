#!/usr/bin/env python3
import bcrypt

def _hash_password(password: str) -> bytes:
    """Generate a salted hash of the input password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
