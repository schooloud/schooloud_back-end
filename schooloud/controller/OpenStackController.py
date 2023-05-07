import openstack


class OpenStackController:
    def __init__(self):
        pass

    def create_admin_connection(self):
        return openstack.connect(
            auth_url="http://211.37.146.151/identity",
            username="admin",
            password="vp2smsehsRktmfh!!",
            project_id="008f771ca9564acaae66fc110e964f75",
            project_name="admin",
            user_domain_name="Default",
            project_domain_name="default",
            region_name="RegionOne",
            interface="public",
            identity_api_version=3
        )