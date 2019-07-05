from flask import Blueprint, jsonify, Response, request
from src.constant import *
from src.model.UserModel import UserModel
from src.out.UserDTO import UserDTO
import json

user_api = Blueprint('user_api', __name__)
userDTO = UserDTO()


@user_api.route(api_url_user_list, methods=['GET'])
def getUserList():
    return Response(json.dumps(userDTO.dump(UserModel.fetchAll(), many=True).data), status=200)


@user_api.route(api_url_user, methods=['GET'])
def getUser(user_id):
    return Response(json.dumps(userDTO.dump(UserModel.fetchByID(user_id)).data), status=200)


@user_api.route(api_url_user_register, methods=['POST'])
def registerUser():
    data  =  userDTO.load(request.get_json())
    userModel = UserModel(data.data)
    userModel.save()
    return Response(json.dumps(userDTO.dump(userModel).data), status=200)