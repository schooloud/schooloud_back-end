from schooloud.blueprints import user
from schooloud.controller.UserController import UserController
from flask import request, make_response
from schooloud.model.user import User

userController = UserController()


@user.route('/login', methods=['POST'])
def login():
    response = make_response()
    response = userController.authenticate(request.get_json(), response)
    return response


@user.route('/logout', methods=['POST'])
def logout():
    # session db update
    return userController


@user.route('/email-check', methods=['POST'])
def emailCheck():
    return userController.check_email(request.get_json())


@user.route('/register', methods=['POST'])
def register():
    return userController.create_user(request.get_json())


@user.route('/list')
def list():
    return userController.get_user_list()
