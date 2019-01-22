"""
The app module, containing the app factory function.
Factory functions allow us to have multiple configurations of the server
(testing, production, etc.)
See http://flask.pocoo.org/docs/1.0/patterns/appfactories/ for more info
"""

from flask import Flask

from backend_site.extensions import cors
from backend_site.settings import ProdConfig

from backend_site.events import blueprint as events_routes
from backend_site.officers import blueprint as officers_routes
from backend_site.projects import blueprint as projects_routes
from .views import blueprint as static_views


def createApp(config_object=ProdConfig):
    """
    Factory method to create new Flask app from the modules in each subfolder
    """
    print(__name__)
    print(__name__.split('.')[0])
    app = Flask(__name__.split('.')[0],
                static_folder=None,
                root_path=config_object.PROJECT_ROOT)
    app.config.from_object(config_object)

    origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')
    cors.init_app(static_views,
                  origins=origins,
                  url_prefix='/')
    cors.init_app(events_routes,
                  origins=origins,
                  url_prefix='/api/events')
    cors.init_app(officers_routes,
                  origins=origins,
                  url_prefix='/api/officers')
    cors.init_app(projects_routes,
                  origins=origins,
                  url_prefix='/api/projects')

    app.register_blueprint(static_views, url_prefix='/')
    app.register_blueprint(events_routes, url_prefix='/api/events')
    app.register_blueprint(officers_routes, url_prefix='/api/officers')
    app.register_blueprint(projects_routes, url_prefix='/api/projects')

    return app
