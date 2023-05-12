from flask import Blueprint


def _factory(partial_module_string, url_prefix):
    name = partial_module_string
    import_name = 'schooloud.api.{}'.format(partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=url_prefix)
    return blueprint


hello = _factory('hello', '/hello_world')
hello_github = _factory('hello_github', '/hello_github')
user = _factory('user', '/api/v1/user')
proposal = _factory('proposal', '/api/v1/proposal')
keypair = _factory('keypair', '/api/v1/keypair')
project = _factory('project', '/api/v1/project')
flavor = _factory('flavor', '/api/v1/flavor')
instance = _factory('instance', '/api/v1/instance')
domain = _factory('domain', '/api/v1/domain')

all_blueprints = (hello, hello_github, proposal, user, keypair, flavor, project, instance, domain)

