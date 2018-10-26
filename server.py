"""
Backend server for LUG@UIC website
"""
from enum import Enum
import json
import re
from flask import Flask, jsonify, request
from flask_cors import CORS

class Positions(Enum):
  """
  List of LUG Officer positions.
  """
  PRESIDENT = "PRESIDENT"
  VICEPRESIDENT = "VICEPRESIDENT"
  TREASURER = "TREASURER"
  MEMBER = "MEMBER"

app = Flask(__name__, static_url_path='/static/', static_folder='frontend-site/dist')

CORS(app)

@app.route('/')
def homePage():
  """
  Route for '/' - Home Page
  """
  return app.send_static_file('index.html')

@app.route('/static/<path:path>')
def sendStatic(path):
  """
  Route for all files under '/static/'
  """
  return app.send_static_file(path)

@app.route('/api')
def appRoot():
  """
  Route for '/api'
  """
  return 'API response here!'

def makeMockPost(title, content):
  """
  TODO: Posting functionality
  """
  post = dict()
  post['title'] = title
  post['content'] = content
  return post

@app.route('/api/posts')
def getPosts():
  """
  API function to retrieve all posts
  """
  posts = [
    makeMockPost('Test post', 'Test post. Please Ignore'),
    makeMockPost('First post', 'This is the first, non-test post'),
    makeMockPost('Foo?', 'Bar.'),
  ]
  return jsonify(posts)

@app.route('/api/officers', methods=['GET'])
def getOfficers():
  """
  API function to retrieve officers
  Parameters:
  /api/officers?position=[PRESIDENT,VICEPRESIDENT,TREASURER]
               ?semester=SEASON_YEAR
                  e.g. "?semester=SUMMER_2018
                  Overrides 'year'
               ?year=<Academic year>
                  e.g. "?year=2018" for Summer 2018 - Spring 2019 inclusive
                  Not read if 'semester' param exists
               ?is_current=[Y,N]
  """

  # Utility functions

  def getSemesterID(semester_string):
    """
    Convert a semester string of the form "SEASON_YEAR" (e.g. "SPRING_2018") into
    a numeric value
    Works by left-shifting the year by 2 and adding a value for the season - fast,
    preserves ordering; can easily get season by testing modulo the season (e.g.
    if id % 4 == 1, season is Summer)
    """
    season, year_str = semester_string.strip().upper().split('_')
    if season == 'SPRING':
      season_id = 0
    elif season == 'SUMMER':
      season_id = 1
    elif season == 'FALL':
      season_id = 2
    else: # Probably an error
      season_id = 3
    semester_id = (int(year_str) << 2) + season_id
    return semester_id

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

  def upperStr(reqstr):
    """
    Utility function to convert input to uppercase string
    """
    return str(reqstr).upper()

  def semesterStr(reqstr):
    """
    Returns None if str is not a semester string, and converts it to standard
    format if it is (TODO)
    Standard format is SEASON_YEAR, e.g. SPRING_2018
    """
    template = re.compile(r'(SPRING|SUMMER|FALL)_\d\d\d\d')
    reqstr = str(reqstr).upper()
    if template.match(reqstr):
      return reqstr
    return None

  # Get officers from json file
  with open('officers.json') as officers_file:
    officers = json.load(officers_file)

  # Filter by position (President etc.)
  position = request.args.get('position', default=None, type=upperStr)
  if position:
    # If invalid position given, error
    if position not in Positions.__members__:
      return jsonify({"error": "Invalid parameter 'position'"}), 400
    officers = [x for x in officers if x["position"] == position]

  # Filter by semester
  semester = request.args.get('semester', default=None, type=semesterStr)
  year = request.args.get('year', default=None, type=int)
  if semester:
    sem_id = getSemesterID(semester)
    def semesterInRange(officer):
      term_start_id = getSemesterID(officer["term_start"])
      term_end_id = getSemesterID(officer["term_end"])
      return term_start_id <= sem_id <= term_end_id
    officers = [x for x in officers if semesterInRange(x)]
  elif not semester and 'semester' in request.args:
    # In this case, a semester parameter was passed but semesterStr failed to
    # match
    return jsonify({"error": "Invalid parameter 'semester'"}), 400
  elif year:
    # Filter by term academic year - semester param overrides this
    # We want all officers whose term began before the end, and ended after the
    # beginning, of this academic year.
    range_start_id = getSemesterID(f'SUMMER_{year}')
    range_end_id = getSemesterID(f'SPRING_{(year + 1)}')
    def yearInRange(officer):
      term_start_id = getSemesterID(officer["term_start"])
      term_end_id = getSemesterID(officer["term_end"])
      return term_start_id < range_end_id and term_end_id > range_start_id
    officers = [x for x in officers if yearInRange(x)]

  # Filter by current student status
  if 'is_current' in request.args:
    is_current_char = request.args.get('is_current', type=upperStr)
    if is_current_char in ('Y', 'T', 'YES', 'TRUE'):
      officers = [x for x in officers if x["current_student"]]
    elif is_current_char in ('N', 'F', 'NO', 'FALSE'):
      officers = [x for x in officers if not x["current_student"]]
    else:
      return jsonify({"error": "Invalid parameter 'is_current'"}), 400

  return jsonify(officers)
