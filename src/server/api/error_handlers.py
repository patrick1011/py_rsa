from flask import Blueprint
from flask import jsonify

blueprint = Blueprint('error_handlers', __name__)


@blueprint.app_errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description})
    return response, 400


@blueprint.app_errorhandler(401)
def custom401(error):
    response = jsonify({'message': error.description})
    return response, 401


@blueprint.app_errorhandler(404)
def custom404(error):
    response = jsonify({'message': error.description})
    return response, 404


@blueprint.app_errorhandler(405)
def custom405(error):
    response = jsonify({'message': error.description})
    return response, 405


@blueprint.app_errorhandler(500)
def custom500(error):
    response = jsonify({'message': 'Internal server error'})
    return response, 500
