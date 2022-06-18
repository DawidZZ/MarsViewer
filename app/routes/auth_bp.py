from flask import Blueprint
from app.controllers.auth_controller import login, register

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route("/auth/login") (login)
auth_bp.route("/auth/register") (register)