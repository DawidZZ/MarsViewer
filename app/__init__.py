from flask import Flask
from config import Config

from app.routes.home_bp import home_bp
from app.routes.auth_bp import auth_bp
from app.routes.gallery_bp import gallery_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(gallery_bp)

from app.routes import error_routes