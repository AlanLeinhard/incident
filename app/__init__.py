
from flask import Flask
# from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from . import config as Config

# from .views import bp 


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    app.config.from_pyfile('config-extended.py')
    CORS(app)
    from . import views

    app.register_blueprint(views.bp)

    return app

def maan():
    app = create_app()
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)


# Ставим редирект, если пользователь не авторизован, для страниц где обязательна авторизация
# login_manager = LoginManager(app)
# login_manager.login_view = 'admin_blueprint.login'

