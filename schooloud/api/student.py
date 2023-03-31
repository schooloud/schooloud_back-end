from flask import Blueprint
from flask import jsonify

from schooloud.model.student import Student

bp = Blueprint('student', __name__, url_prefix='/student')


@bp.route('/<sid>')
def say_hello_world(sid):
    student = Student.query.filter(Student.sid == sid).one()
    student_dict = {
        'sid': student.sid,
        'email': student.email,
        'name': student.name,
        'password': student.password,
        'major': student.major
    }
    return jsonify(student_dict)
