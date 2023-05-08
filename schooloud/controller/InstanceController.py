from schooloud.model.instance import Instance
from schooloud.controller.OpenStackController import OpenStackController
import pprint

openstack_controller = OpenStackController()


class InstanceController:
    def __init__(self):
        pass

    def create_instance(self):
        return

    def unpause_instance(self):
        return

    def pause_instance(self):
        return

    def delete_instance(self):
        return

    def reboot_instance(self):
        return

    def get_instance_list(self, user_email, project_id):
        conn = openstack_controller.create_connection(user_email)


        return

    def get_instance_detail(self):
        return
