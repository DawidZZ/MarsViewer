from flask import Blueprint
from app.controllers.home_controller import home

home_bp = Blueprint('home_bp', __name__)

home_bp.route('/') (home)