from sqlalchemy.exc import NoResultFound

from schooloud.model.user import User

from schooloud.libs.database import db

from flask import jsonify, Response, abort

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
        try:
            user = User.query.filter(User.email == params['email']).one()
            if user.password != params['password']:
                return abort(404)
            else:
                # Cookie creation
                return user.email
        except NoResultFound:
            return abort(404)

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
            user = User.query.filter(User.email == params['email']).one()
            return abort(404)
        except NoResultFound:
            return Response("",status=200,mimetype='application/json')

    # 유저 전체 목록
    def get_user_list(self):
        users = User.query.all()
        user_list = []
        for user in users:
            user_list.append({
                "email":user.email,
                "name":user.name,
                "major":user.major,
                "studentId":user.studentId,
                "role":user.role
            })
        return jsonify({"users":user_list})

