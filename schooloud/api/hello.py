from schooloud.blueprints import hello
from schooloud.controller.UserController import UserController


uc = UserController()

@hello.route('/say')
def say_hello_world():
    uc.get_user()
    return 'Hello World!'


