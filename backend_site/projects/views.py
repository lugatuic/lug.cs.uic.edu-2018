from flask import Blueprint

blueprint = Blueprint('projects', __name__)


@blueprint.route('/', methods=['GET'])
def getProjects():
    with open('projects.json') as projects_file:
        return projects_file.read()
