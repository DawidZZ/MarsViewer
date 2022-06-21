from flask import Blueprint
from app.controllers.auth_controller import login, register, logout

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route("/auth/login/", methods=['GET', 'POST']) (login)
auth_bp.route("/auth/register/", methods=['GET', 'POST']) (register)
auth_bp.route("/auth/logout/") (logout)