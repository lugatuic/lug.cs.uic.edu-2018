"""API routes for the Projects record type"""
import json
from flask import Blueprint,jsonify
from flask_cors import CORS

blueprint = Blueprint('projects', __name__)
CORS(blueprint)


@blueprint.route('', methods=['GET'])
def getProjects():
    """Route to retrieve all LUG projects, past and present"""
    with open('projects.json') as projects_file:
        projects=projects_file.read()
        projects=json.loads(projects)
        return jsonify (projects)
