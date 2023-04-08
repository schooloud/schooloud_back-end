from schooloud.blueprints import student
from schooloud.controller.TestController import TestController
from flask import jsonify


testcontroller = TestController()


@student.route('/<sid>')
def say_hello_world(sid):
    student = testcontroller.get_test_user(sid)
    return jsonify(student)
