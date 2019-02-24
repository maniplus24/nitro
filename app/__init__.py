import datetime

from flask import Flask

import jwt

from View.Billing.billing_views import billing_blueprint
from View.User.user_views import user_blueprint
from app.routes import init_api_routes
from instance.config import BaseConfig

api = Flask(__name__)


secret_key = BaseConfig.SECRET_KEY

api.register_blueprint(user_blueprint)
api.register_blueprint(billing_blueprint)


@api.route('/login', methods=['GET'])
def get_token():
    expiration_date = (datetime.datetime.utcnow() + datetime.timedelta(days=1))
    token = jwt.encode({'exp': expiration_date}, secret_key, algorithm='HS256')
    return token


if __name__ == '__main__':
    api.run()
