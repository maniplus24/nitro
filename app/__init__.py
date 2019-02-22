import datetime

from flask import Flask


import jwt

from app.routes import init_api_routes
from instance.config import BaseConfig

api = Flask(__name__)

init_api_routes(api)

secret_key = BaseConfig.SECRET_KEY


@api.route('/login', methods=['GET'])
def get_token():
    expiration_date = (datetime.datetime.utcnow() + datetime.timedelta(days=1))
    token = jwt.encode({'exp': expiration_date}, secret_key, algorithm='HS256')
    return token


if __name__ == '__main__':
    api.run()
