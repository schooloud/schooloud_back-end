from schooloud.model.student import Student


class TestController:
    def __init__(self):
        pass

    def get_test_user(self, sid):
        student = Student.query.filter(Student.sid == sid).one()
        student_dict = {
            'sid': student.sid,
            'email': student.email,
            'name': student.name,
            'password': student.password,
            'major': student.major
        }
        return student_dict
