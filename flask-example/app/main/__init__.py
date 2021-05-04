from flask import Blueprint

# Blueprint Configuration
main_bp = Blueprint(
    'main', __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes