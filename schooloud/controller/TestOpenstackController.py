from schooloud.model.student import Student
import openstack
import argparse
import os
import sys

class TestOpenstackController:
    def __init__(self):
        pass

    def create_connection_from_config(self, TEST_CLOUD):
        return openstack.connect(cloud=TEST_CLOUD)

    def create_connection(auth_url, region, project_name, username, password,
                          user_domain, project_domain):
        return openstack.connect(
            auth_url=auth_url,
            project_name=project_name,
            username=username,
            password=password,
            region_name=region,
            user_domain_name=user_domain,
            project_domain_name=project_domain,
            app_name='examples',
            app_version='1.0',
        )
    def get_instance_list(self, conn):
        instance_list = []
        for server in conn.compute.servers():
            instance_list.append(server.to_dict())
        return instance_list

    def get_instance(self, conn, instanceId):
        return conn.get_server(name_or_id=instanceId)

    def pause_instance(self, conn, instanceId):
        instance = self.get_instance(conn, instanceId)
        if instance['status'] == 'ACTIVE':
            conn.compute.pause_server(instance['id'])
            return True
        return False

    def unpause_instance(self, conn, instanceId):
        instance = self.get_instance(conn, instanceId)
        if instance['status'] == 'PAUSE':
            conn.compute.unpause_server(instance['id'])
            return True
        return False