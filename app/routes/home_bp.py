from flask import Blueprint
from app.controllers.home_controller import index, favicon

home_bp = Blueprint('home_bp', __name__)

home_bp.route('/') (index)
home_bp.route('/favicon.ico') (favicon)
