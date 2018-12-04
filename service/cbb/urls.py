from flask import Blueprint
from .views import CbbView


site = Blueprint('cbb', __name__, url_prefix='/api')

site.add_url_rule('/cbb', view_func=CbbView.as_view('cbb'))
