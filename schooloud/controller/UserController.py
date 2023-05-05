from sqlalchemy.exc import NoResultFound

from schooloud.model.user import User

from schooloud.libs.database import db

class UserController:
    def __init__(self):
        pass

    # 유저 반환
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

    # 로그인
    def authenticate(self, params):
        user = User.query.filter(User.email == params['email']).one()
        if user.password != params['password']:
            return False
        else:
            return user

    # 회원가입
    def create_user(self, params):
        user = User(
            email=params['email'],
            studentId=params['studentId'],
            name=params['name'],
            password=params['password'],
            major=params['major'],
            role=params['role']
        )
        db.session.add(user)
        db.session.commit()
        return user.email

    # 이메일 중복 체크
    def check_email(self, params):
        try:
            user = User.query.filter(User.email==params['email']).one()
            return False
        except NoResultFound:
            return True

    # 유저 전체 목록
    def get_user_list(self):
        users = User.query.all()
        return users

