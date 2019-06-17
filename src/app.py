from flask import Flask
from src.views.UserView import user_api
from src.constant import *


def application():
    app = Flask(__name__)
    app.register_blueprint(user_api, url_prefix=api_url_user_prefix)

    return app
