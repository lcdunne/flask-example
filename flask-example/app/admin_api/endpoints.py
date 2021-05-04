from . import api_bp


@api_bp.route('/resource')
def resource():
    return {'msg': 'Hi'}
