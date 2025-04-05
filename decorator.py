from functools import wraps
from flask import jsonify, session


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"message": "Unauthorized. Please Log in!"}), 401

        return fn(*args, **kwargs)
    
    return wrapper

def role_required(required_role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if "user_id" not in session:
                return jsonify({"message": "Unauthorized"}), 401
            if session.get("role") != required_role:
                return jsonify({"message": f"Access denied. Requires role: {required_role}"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator