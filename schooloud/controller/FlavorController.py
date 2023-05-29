from schooloud.controller.OpenStackController import OpenStackController
import pprint

openstack_controller = OpenStackController()


class FlavorController:
    def __init__(self):
        pass

    def get_flavor_list(self, user_email):
        def ram_format(ram):
            if ram > 512:
                return str(ram // 1024) + 'GB'
            else:
                return str(ram) + 'MB'

        conn = openstack_controller.create_admin_connection()
        allow_flavors = ['m1.micro', 'm1.tiny', 'm1.small', 'cirros256']
        flavors = []
        for flavor in conn.compute.flavors():
            if flavor['name'] in allow_flavors:
                f = {'id': flavor['id'],
                     'name': flavor['name'],
                     'ram': ram_format(flavor['ram']),
                     'disk': str(flavor['disk']) + 'GB',
                     'cpu': str(flavor['vcpus'])
                     }
                flavors.append(f)
        return {"flavors": flavors}
