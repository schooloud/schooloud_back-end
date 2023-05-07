from schooloud.blueprints import keypair
from schooloud.controller.KeypairController import KeypairController
from flask import request, abort

keypairController = KeypairController()

@keypair.route('/create', methods=['POST'])
def create_keypair():
    print(request.cookies.get('email'))
    return keypairController.create_keypair(request.get_json(), request.cookies.get('email'))

@keypair.route('/list', methods=['POST'])
def keypair_list():
    return keypairController.keypair_list(request.cookies.get('email'))
