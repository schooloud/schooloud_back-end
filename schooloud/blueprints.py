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

all_blueprints = (hello, hello_github, proposal, user, keypair)
