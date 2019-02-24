from functools import wraps

import jwt
from flask import jsonify, request
from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

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


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):

            class ValidateInputs(Inputs):
                json = [JsonSchema(schema=schema_name)]

            inputs = ValidateInputs(request)

            if not inputs.validate():
                return jsonify(success=False, errors=inputs.errors)

            return f(*args, **kw)
        return wrapper
    return decorator
