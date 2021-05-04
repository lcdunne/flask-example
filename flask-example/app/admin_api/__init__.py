from flask import Blueprint

# Blueprint Configuration
api_bp = Blueprint(
    'api', __name__,
    template_folder='templates',
    static_folder='static'
)
