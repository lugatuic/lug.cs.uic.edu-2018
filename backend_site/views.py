"""Basic routes for static resources"""

from flask import Blueprint
from .settings import STATIC_DIR, STATIC_ROUTE

blueprint = Blueprint('static', __name__,
                      static_folder=STATIC_DIR,
                      static_url_path=STATIC_ROUTE)

# print("Static blueprint root path:")
# print(blueprint.root_path)
# print("Static blueprint static directory:")
# print(blueprint.static_folder)


@blueprint.route('/')
def homePage():
    """Route for '/' - Home Page"""
    # print("Firing homepage route!")
    # print(blueprint.root_path)
    # print(blueprint.static_folder)
    return blueprint.send_static_file('index.html')


@blueprint.route('/static/<path:req_path>')
def sendStatic(req_path):
    """Route for all files under '/static/'"""
    # print("Firing static route!")
    return blueprint.send_static_file(req_path)


@blueprint.route('/api')
def appRoot():
    """Route for '/api'"""
    return 'API response here!'
