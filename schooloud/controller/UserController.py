from schooloud.model.user import User


class UserController:
    def __init__(self):
        pass

    def get_user(self, email):
        user = User.query.filter(User.email == email).one()
        user_dict = {
            'studentId': user.studentId,
            'name': user.name,
            'password': user.password,
            'major': user.major,
            'role': user.role
        }
        return user_dict
