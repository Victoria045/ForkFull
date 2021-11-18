from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User

# Creating app instance
app = create_app('development')

app.config.update(dict(
    SECRET_KEY="SECRET_KEY=9b02a34f4cea78c4a8b8b0429c543d34",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

manager = Manager(app)

manager.add_command('server', Server)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)

@manager.command 
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().dicsover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User=User)

if __name__ == '__main__':
    manager.run()