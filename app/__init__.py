from flask import Flask
from config import Config

from app.routes.home_bp import home_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home_bp)