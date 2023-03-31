from flask import Blueprint

bp = Blueprint('hello_world', __name__, url_prefix='/hello_world')


@bp.route('/say')
def say_hello_world():
    return 'Hello World!'


