from flask import Blueprint

category_api_blueprint = Blueprint("category_api", __name__)

from . import routes
