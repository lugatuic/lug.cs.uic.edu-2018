"""
Extension objects used by Flask app
We cannot create these objects in the application factory
See http://flask.pocoo.org/docs/1.0/patterns/appfactories/#factories-extensions
"""

from flask_cors import CORS

cors = CORS()
