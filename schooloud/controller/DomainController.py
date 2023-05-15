import requests
import os
from schooloud.model.instance import Instance
from schooloud.controller.OpenStackController import OpenStackController
from schooloud.libs.database import db

openstack_controller = OpenStackController()


class DomainController:
    def __init__(self):
        pass

    def assign_domain(self, request_data, user_email):
        app_key = os.environ['APP_KEY']
        project_id = request_data['project_id']
        instance_id = request_data['instance_id']
        domain = request_data['domain']

        # check if same domain exists
        query = Instance.query.filter(Instance.domain == domain+'.schooloud.cloud.')
        if db.session.query(query.exists()).scalar():
            return {"message": "ERROR: The same domain already exists"}

        # openstack connection
        conn = openstack_controller.create_connection_with_project_id(user_email, project_id)

        # get instance floating_ip
        floating_ip = ''
        instance = conn.compute.find_server(instance_id)
        for ip in instance['addresses']['private']:
            if ip['OS-EXT-IPS:type'] == 'floating':
                floating_ip = ip['addr']
        if floating_ip == '':
            return {"message": "ERROR: instance doesn't have floating ip"}

        # create record set
        data = {"recordset": {"recordsetName": domain + ".schooloud.cloud.",
                              "recordsetType": "A",
                              "recordsetTtl": 60,
                              "recordList": [{"recordDisabled": False,
                                              "recordContent": floating_ip}]}}

        # get DNS_zone from NHN cloud
        dns_zone_list = requests.get(
            f'https://dnsplus.api.nhncloudservice.com/dnsplus/v1.0/appkeys/{app_key}/zones').json()
        dns_zone_id = dns_zone_list['zoneList'][0]['zoneId']

        # request record set to NHN cloud
        response = requests.post(
            f'https://dnsplus.api.nhncloudservice.com/dnsplus/v1.0/appkeys/{app_key}/zones/{dns_zone_id}/recordsets',
            json=data).json()

        if not response['header']['isSuccessful']:
            return {"message": "ERROR: can't create record set"}
        domain_id = response['recordset']['recordsetId']
        domain = response['recordset']['recordsetName']

        # add domain to database
        instance = Instance.query.filter(Instance.instance_id == instance_id).one()
        instance.domain = domain
        instance.domain_id = domain_id
        db.session.commit()

        return ''

    def get_domain_list(self):
        return

    def get_port_list(self):
        return
