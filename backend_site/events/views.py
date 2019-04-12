"""API routes for the Events record type"""

from flask import Blueprint, jsonify
from flask_cors import CORS
from requests import HTTPError

from .models import getCacheEvents

blueprint = Blueprint('views', __name__)
CORS(blueprint)


@blueprint.route('', methods=['GET'])
def getEvents():
    """Route for /api/events"""
    try:
        return jsonify(getCacheEvents())
    except HTTPError:
        return (
            jsonify({"error": "Failed to download upstream calendar file"}),
            502
        )
    except KeyError:
        return (
            jsonify({"error": "One or more calendar events are missing an expected property"}),
            500
        )
