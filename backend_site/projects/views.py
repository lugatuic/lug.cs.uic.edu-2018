"""API routes for the Projects record type"""

from flask import Blueprint

blueprint = Blueprint('projects', __name__)


@blueprint.route('/', methods=['GET'])
def getProjects():
    """Route to retrieve all LUG projects, past and present"""
    with open('projects.json') as projects_file:
        return projects_file.read()
