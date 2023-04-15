from schooloud.blueprints import hello


@hello.route('/say')
def say_hello_world():
    return 'Hello World!'


