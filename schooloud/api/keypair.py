from schooloud.blueprints import keypair
from schooloud.controller.KeypairController import KeypairController
from flask import request, abort

from schooloud.libs.decorator import session_authenticate

keypairController = KeypairController()


@keypair.route('/create', methods=['POST'])
@session_authenticate
def create_keypair(**kwargs):
    return keypairController.create_keypair(request.get_json(), kwargs['email'])


@keypair.route('/list')
@session_authenticate
def keypair_list(**kwargs):
    return keypairController.keypair_list(kwargs['email'])
