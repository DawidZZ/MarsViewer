from flask import Blueprint
from app.controllers.gallery_controller import main_page, user_collection

gallery_bp = Blueprint('gallery_bp', __name__)

gallery_bp.route('/gallery/main') (main_page)
gallery_bp.route('/gallery/favourite') (user_collection)