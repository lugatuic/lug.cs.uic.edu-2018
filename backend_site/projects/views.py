"""API routes for the Projects record type"""

from flask import Blueprint
from flask_cors import CORS

blueprint = Blueprint('projects', __name__)
CORS(blueprint)


@blueprint.route('', methods=['GET'])
def getProjects():
    """Route to retrieve all LUG projects, past and present"""
    with open('projects.json') as projects_file:
        return projects_file.read()
