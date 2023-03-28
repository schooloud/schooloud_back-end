import os
import sys

from flask_script import Manager

from schooloud import app, init_app

manager = Manager(app)


# migrate = Migrate(app)

@manager.command
def runserver():
    config = app.config
    init_app(app)
    app.run(config['HOST'], config['PORT'], Debug=config['DEBUG'])


if __name__ == "__main__":
    # Set Python Working directory to backend package path
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    if sys.argv[1] == 'db':
        init_app(app)

    manager.run()
