from schooloud.model.instance import Instance
from schooloud.model.project import Project
from schooloud.controller.OpenStackController import OpenStackController
from schooloud.libs.database import db

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
        network = conn.network.find_network('private')
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
        if project.memory < current_ram_usage + flavor['ram'] / 1024:
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

        conn.compute.wait_for_server(instance)

        # assign floating ip to instance
        ################################# 추가 필요

        # add instance to database
        instance = Instance(instance_id=instance.id,
                            project_id=project_id)
        db.session.add(instance)
        db.session.commit()

        return {"instance_id": instance.instance_id}

    def unpause_instance(self, request_data, user_email):
        project_id = request_data['project_id']
        instance_id = request_data['instance_id']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # unpause instance
        instance = conn.compute.find_server(instance_id)
        if instance.status == 'PAUSED':
            conn.compute.unpause_server(instance)
        else:
            return {"message": "cannot unpause server"}

        return ''

    def pause_instance(self, request_data, user_email):
        project_id = request_data['project_id']
        instance_id = request_data['instance_id']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # pause instance
        instance = conn.compute.find_server(instance_id)
        if instance.status == 'ACTIVE':
            conn.compute.pause_server(instance)
        else:
            return {"message": "cannot pause server"}

        return ''

    def delete_instance(self, request_data, user_email):
        project_id = request_data['project_id']
        instance_id = request_data['instance_id']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # delete instance
        instance = conn.compute.find_server(instance_id)
        conn.compute.delete_server(instance)

        # return floating ip from openstack
        ############################ 추가 필요

        # delete from database
        Instance.query.filter(Instance.instance_id == instance_id).delete()
        db.session.commit()

        return ''

    def reboot_instance(self, request_data, user_email):
        project_id = request_data['project_id']
        instance_id = request_data['instance_id']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # reboot instance
        instance = conn.compute.find_server(instance_id)
        if instance.status == 'ACTIVE':
            conn.compute.reboot_server(instance, 'SOFT')
        elif instance.status == 'PAUSED':
            conn.compute.reboot_server(instance, 'HARD')
        else:
            return {"message": "cannot reboot server"}

        return {"message": "successfully rebooted"}

    def get_instance_list(self, request_data, user_email):
        project_id = request_data['project_id']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # get instance list
        instance_list = []
        for server in conn.compute.servers():
            instance = {
                "instance_id": server.id,
                "instance_name": server.name,
                "image_name": conn.image.find_image(server.image.id).name,
                "flavor": server.flavor['original_name'],
                "keypair_name": server.key_name,
                "status": server.status,
                "ip_addresses": []
            }

            # get instance's ip address
            for ip in server.addresses['private']:
                instance['ip_addresses'].append(ip['addr'])

            # get instance domain
            domain = Instance.query.filter(Instance.instance_id == server.id).one().domain
            instance['domain'] = domain

            instance_list.append(instance)

        return {"instance_list": instance_list}

    def get_instance_detail(self, request_data, user_email):
        project_id = request_data['project_id']
        instance_id = request_data['instance_id']

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # get instance
        instance = conn.compute.find_server(instance_id)

        response = {
            "instance_id": instance.id,
            "instance_name": instance.name,
            "image_name": conn.image.find_image(instance.image.id).name,
            "flavor": instance.flavor['original_name'],
            "keypair_name": instance.key_name,
            "status": instance.status,
            "ip_addresses": []
        }

        # get instance's ip address
        for ip in instance.addresses['private']:
            response['ip_addresses'].append(ip['addr'])

        # get instance domain
        domain = Instance.query.filter(Instance.instance_id == instance_id).one().domain
        response['domain'] = domain

        return response
