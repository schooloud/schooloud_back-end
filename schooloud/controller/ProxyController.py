from schooloud.model.instance import Instance


class ProxyController:
    def __init__(self):
        pass

    def get_instance(self, instanceId):
        instance = Instance.query.filter(Instance.instanceId == instanceId).one()
        instance_dict = {
            'domain': instance.domain,
            'port': instance.port,
            'projectId': instance.projectId
        }
        return instance_dict
