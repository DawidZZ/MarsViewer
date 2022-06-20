from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.routes.home_bp import home_bp
from app.routes.auth_bp import auth_bp
from app.routes.gallery_bp import gallery_bp

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(gallery_bp)

from app.models.user import User
from app.routes import error_routes