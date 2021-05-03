from flask import Blueprint
# from app import db
# from app.models import User


# Blueprint Configuration
api_bp = Blueprint(
    'api', __name__,
    template_folder='templates',
    static_folder='static'
)


@api_bp.route('/resource')
def resource():
    return {'msg': 'Hi'}
