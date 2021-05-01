'''Manage to assist migrations.
See:
    - https://flask-migrate.readthedocs.io/en/latest/
    - https://gist.github.com/mayukh18/2223bc8fc152631205abd7cbf1efdd41/

This allows to run the following with terminal:
    $ python manage.py db init
    $ python manage.py db migrate
    $ python manage.py db upgrade'''

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
