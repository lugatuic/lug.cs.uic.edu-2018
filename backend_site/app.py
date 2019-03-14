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


# def corsInit(routes, origins):
#     """Initialize CORS headers for all routes"""
#     for (route, path) in routes:
#         cors.init_app(route, origins=origins, url_prefix=path)

def registerBlueprints(routes, app):
    """Register blueprints to app for all routes"""
    for (route, path) in routes:
        app.register_blueprint(route, url_prefix=path)

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

    # origins = app.config.get('CORS_ORIGIN_WHITELIST', '*')

    routes = [
        (static_views, '/'),
        (events_routes, '/api/events'),
        (officers_routes, '/api/officers'),
        (projects_routes, '/api/projects')
    ]

    # corsInit(routes, origins)
    registerBlueprints(routes, app)

    return app
