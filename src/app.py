from flask import Flask, jsonify, make_response
from src.views.UserView import user_api
from src.constant import api_url_user_prefix
from .config import Config
from .model import db


def application():
    app = Flask(__name__)
    app.register_blueprint(user_api, url_prefix=api_url_user_prefix)
    app.config.from_object(Config)
    db.init_app(app)

    @app.errorhandler(404)
    def error404(error):
        return make_response(jsonify({'message': 'Requested page not found!'}), 404)

    return app
