from functools import wraps

import jwt
from flask import jsonify, request

from instance.config import BaseConfig

secret_key = BaseConfig.SECRET_KEY


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            token = request.headers['Authorization']
        except KeyError:
            return jsonify({"Error": "No Token"})
        try:
            jwt.decode(token, secret_key, algorithms='HS256')
        except:
            return jsonify({"Error": "Invalid Token"})
        return f(*args, **kwargs)
    return wrapper
