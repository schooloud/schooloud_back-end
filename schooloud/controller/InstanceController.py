from schooloud.model.instance import Instance
from schooloud.model.project import Project
from schooloud.controller.OpenStackController import OpenStackController
import pprint

openstack_controller = OpenStackController()


class InstanceController:
    def __init__(self):
        pass

    def create_instance(self, request_data, user_email):
        project_id = request_data['project_id']
        instance_name = request_data['instance_name']
        image_name = request_data['image_name']
        flavor_name = request_data['flavor_name']
        keypair_name = request_data['keypair_name']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # find image, flavor, network, keypair from openstack
        image = conn.image.find_image(image_name)
        flavor = conn.compute.find_flavor(flavor_name)
        network = conn.network.find_network('shared')
        keypair = conn.compute.find_keypair(keypair_name)

        # project quata check
        current_cpu_usage, current_ram_usage, current_disk_usage = 0, 0, 0
        for server in conn.compute.servers():
            current_cpu_usage += server.flavor['vcpus']
            current_ram_usage += server.flavor['ram'] / 1024
            current_disk_usage += server.flavor['disk']

        project = Project.query.filter(Project.project_id == project_id).one()
        if project.cpu < current_cpu_usage + flavor['vcpus']:
            return {"message": "exceed cpu usage"}
        if project.memory < current_ram_usage + flavor['ram']/1024:
            return {"message": "exceed memory usage"}
        if project.storage < current_disk_usage + flavor['disk']:
            return {"message": "exceed disk usage"}

        # create instance
        instance = conn.compute.create_server(name=instance_name,
                                              image_id=image.id,
                                              flavor_id=flavor.id,
                                              networks=[{"uuid": network.id}],
                                              key_name=keypair.name
                                              )

        instance = conn.compute.wait_for_server(instance)

        return '200'

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
