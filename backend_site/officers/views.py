"""API Routes for the Officer record type"""

import re
import json
from flask import Blueprint, jsonify, request
from .models import Officer, OfficersParams, Positions, getSemesterID

blueprint = Blueprint('officers', __name__)


def getSemesterString(semester_id):
    """
    Convert numeric semester_id into human-readable string
    """
    year = semester_id >> 2
    season_id = semester_id % 4
    if season_id == 0:
        return "SPRING_" + year
    if season_id == 1:
        return "SUMMER_" + year
    if season_id == 2:
        return "FALL_" + year
    return "UNKNOWN_" + year


def semesterIDType(reqstr):
    """
    Returns None if reqstr is not a semester string, and converts it to
    standard format if it is.
    Standard format is SEASON_YEAR, e.g. SPRING_2018
    TODO: accept more formats
    """
    template = re.compile(r'(SPRING|SUMMER|FALL)_\d\d\d\d')
    reqstr = str(reqstr).upper()
    if template.match(reqstr):
        return getSemesterID(reqstr)
    return None


@blueprint.route('/', methods=['GET'])
def getOfficers():
    """
    API function to retrieve officers
    Parameters:
    /api/officers?position=[PRESIDENT,VICE_PRESIDENT,TREASURER]
               ?semester=SEASON_YEAR
                  e.g. "?semester=SUMMER_2018
                  Overrides 'year'
               ?year=<Academic year>
                  e.g. "?year=2018" for Summer 2018 - Spring 2019 inclusive
                  Not read if 'semester' param exists
               ?is_current_student=[Y,N] - TODO
    """

    # Get officers from json file
    with open('officers.json') as officers_file:
        officers = json.load(officers_file, object_hook=Officer)

    # Filter by position (President etc.)
    position = request.args.get(OfficersParams.POSITION.value,
                                default=None,
                                type=(lambda x: str(x).upper()))
    if position:
        # If invalid position given, error
        if position not in Positions.__members__:
            return jsonify({"error": "Invalid parameter 'position'"}), 400
        officers = [x for x in officers if x.position == position]

    # Filter by semester
    semester = request.args.get(OfficersParams.SEMESTER.value,
                                default=None,
                                type=semesterIDType)
    year = request.args.get(OfficersParams.YEAR.value,
                            default=None,
                            type=int)

    if semester:
        officers = [x for x in officers if x.served_during_semester(semester)]
    elif not semester and OfficersParams.SEMESTER.value in request.args:
        # In this case, a semester parameter was passed but semesterStr failed
        # to match
        return jsonify({"error": "Invalid parameter 'semester'"}), 400
    elif year:
        # Filter by term academic year - semester param overrides this
        # We want all officers whose term began before the end, and ended after
        # the beginning, of this academic year.
        officers = [x for x in officers if x.served_during_year(year)]

    # TODO: Filter by current student status
    # if OfficersParams.IS_CURRENT_STUDENT.value in request.args:
    #   is_current_char = request.args.get(
    #       OfficersParams.IS_CURRENT_STUDENT.value,
    #       type=upperStr)
    #   if is_current_char in ('Y', 'T', 'YES', 'TRUE'):
    #     pass
    #   elif is_current_char in ('N', 'F', 'NO', 'FALSE'):
    #     pass
    #   else:
    #     return jsonify({"error": "Invalid parameter 'is_current'"}), 400

    # Convert Officer objects back to dictionaries before returning
    return jsonify([x.__dict__ for x in officers])
