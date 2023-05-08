from schooloud.blueprints import keypair
from schooloud.controller.KeypairController import KeypairController
from flask import request, abort

from schooloud.libs.decorator import session_authenticate

keypairController = KeypairController()

@keypair.route('/create', methods=['POST'])
@session_authenticate
def create_keypair():
    return keypairController.create_keypair(request.get_json(), request.cookies.get('email'))

@keypair.route('/list', methods=['POST'])
@session_authenticate
def keypair_list():
    return keypairController.keypair_list(request.cookies.get('email'))
