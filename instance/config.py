from flask import Config


class BaseConfig(Config):
    SECRET_KEY = 'secretkey'
