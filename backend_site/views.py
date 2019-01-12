"""Basic routes for static resources"""

from flask import Blueprint
from .settings import PROJECT_ROOT, STATIC_DIR, STATIC_ROUTE

blueprint = Blueprint('static', __name__,
                      static_folder=STATIC_DIR,
                      static_url_path=STATIC_ROUTE)

print(blueprint.root_path)
print(blueprint.static_folder)

@blueprint.route('/')
def homePage():
  """
  Route for '/' - Home Page
  """
  print(blueprint.root_path)
  print(blueprint.static_folder)
  return blueprint.send_static_file('index.html')

@blueprint.route('/static/<path:path>')
def sendStatic(req_path):
  """
  Route for all files under '/static/'
  """
  return blueprint.send_static_file(req_path)

@blueprint.route('/api')
def appRoot():
  """
  Route for '/api'
  """
  return 'API response here!'
