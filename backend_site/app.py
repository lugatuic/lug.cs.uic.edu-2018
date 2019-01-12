"""
The app module, containing the app factory function.
Factory functions allow us to have multiple configurations of the server
(testing, production, etc.)
See http://flask.pocoo.org/docs/1.0/patterns/appfactories/ for more info
"""

from flask import Flask

from backend_site import officers, posts
from backend_site import views as static_views
from backend_site.extensions import cors
from backend_site.settings import ProdConfig

def createApp(config_object=ProdConfig):
  print(__name__)
  print(__name__.split('.')[0])
  app = Flask(__name__.split('.')[0], static_folder=None, root_path=config_object.PROJECT_ROOT)
  # app = Flask(__name__, static_folder=None)
  app.config.from_object(config_object)

  origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
  cors.init_app(static_views.blueprint, origins=origins)
  cors.init_app(officers.views.blueprint, origins=origins, url_prefix='/api/officers')
  cors.init_app(posts.views.blueprint, origins=origins, url_prefix='/api/posts')

  app.register_blueprint(static_views.blueprint)
  app.register_blueprint(officers.views.blueprint)
  app.register_blueprint(posts.views.blueprint)

  return app

