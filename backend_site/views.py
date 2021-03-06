"""Basic routes for static resources"""

from flask import Blueprint
from .settings import STATIC_DIR, STATIC_ROUTE

blueprint = Blueprint('static', __name__,
                      static_folder=STATIC_DIR,
                      static_url_path=STATIC_ROUTE)

# No CORS on static routes!

print("Static blueprint root path:")
print(blueprint.root_path)
print("Static blueprint static directory:")
print(blueprint.static_folder)


@blueprint.route('')
def homePage():
    """Route for '/' - Home Page"""
    return blueprint.send_static_file('index.html')


@blueprint.route('/static/<path:req_path>')
def sendStatic(req_path):
    """Route for all files under '/static/'"""
    return blueprint.send_static_file(req_path)


@blueprint.route('/api')
def appRoot():
    """Route for '/api'"""
    return 'API response here!'
