from schooloud.controller.OpenStackController import OpenStackController

from flask import jsonify
openstack_controller = OpenStackController()
class KeypairController:
    def __init__(self):
        pass

    def create_keypair(self, body_params, email):
        # Create keypair
        conn = openstack_controller.create_connection(email)
        private_key = conn.create_keypair(body_params['keypair_name'])

        return jsonify({"private_key":private_key.private_key})

    def keypair_list(self, email):
        conn = openstack_controller.create_connection(email)
        keys = conn.list_keypairs()
        key_list = []

        for key in keys:
            key_list.append(key.name)

        return jsonify({"key_list":key_list})



