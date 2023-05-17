from schooloud.blueprints import user
from schooloud.controller.UserController import UserController

from flask import request, make_response, abort

from schooloud.libs.decorator import session_authenticate
from schooloud.model.user import User

userController = UserController()


@user.route('/login', methods=['POST'])
def login():
    cookie_data = userController.authenticate(request.get_json())
    response = make_response(cookie_data)

    # set cookie
    for key, value in cookie_data.items():
        response.set_cookie(key, value)
    return response


@user.route('/logout', methods=['POST'])
def logout():
    return userController.user_logout(request.cookies.get('session_key'))


@user.route('/email-check', methods=['POST'])
def emailCheck():
    return userController.check_email(request.get_json())


@user.route('/register', methods=['POST'])
def register():
    try:
        return userController.create_user(request.get_json())
    except:
        return abort(404)


@user.route('/list')
@session_authenticate
def list():
    return userController.get_user_list()
