from flask import Blueprint


def _factory(partial_module_string, url_prefix):
    name = partial_module_string
    import_name = 'schooloud.api.{}'.format(partial_module_string)
    blueprint = Blueprint(name, import_name, url_prefix=url_prefix)
    return blueprint


hello = _factory('hello', '/hello_world')
student = _factory('student', '/student')
hello_github = _factory('hello_github', '/hello_github')


all_blueprints = (hello, student, hello_github)
