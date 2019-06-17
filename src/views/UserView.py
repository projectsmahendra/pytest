from flask import Blueprint, jsonify
from src.constant import api_url_user_list

user_api = Blueprint('user_api', __name__)

data = [
    {
        'id': 1,
        'name': 'user1'
    },
    {
        'id': 2,
        'name': 'user2'
    },
]


@user_api.route(api_url_user_list)
def userList():
    return jsonify(data)
