<<<<<<< HEAD
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
  # NOTE: remember to update ordering in frontend project
  PRESIDENT = "PRESIDENT"
  VICE_PRESIDENT = "VICE_PRESIDENT"
  TREASURER = "TREASURER"
  SECRETARY = "SECRETARY"
  TECHNICAL_OFFICER = "TECHNICAL_OFFICER"
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

@app.route('/api/officers', methods=['GET'])
def getOfficers():
  """
  API function to retrieve officers
  Parameters:
  /api/officers?position=[PRESIDENT,VICE_PRESIDENT,TREASURER,SECRETARY,TECHNICAL_OFFICER]
               ?semester=SEASON_YEAR
                  e.g. "?semester=SUMMER_2018
                  Overrides 'year'
               ?year=<Academic year>
                  e.g. "?year=2018" for Summer 2018 - Spring 2019 inclusive
                  Not read if 'semester' param exists
               ?is_current_student=[Y,N] - TODO
  """

  class Officer():
    """
    Represents Officer objects from the json file
    Used by json.load() - see 'object_hook' in the Python docs
    """
    def __init__(self, d):
      # d is the dictionary passed by json.load()
      self.name = str(d['name'])
      self.position = d['position']
      self.description = str(d['description'])
      self.github = d['github']
      self.slack = str(d['slack'])
      self.personal_site = d['personal_site']
      self.image = d['image']
      self.special_ability = str(d['special_ability'])
      self.join_date = d['join_date']
      self.term_start = d['term_start']
      self.term_end = d['term_end']
      self.graduating_semester = d['graduating_semester']

    def term_start_id(self):
      """
      Convert term_start semester string to numeric ID
      """
      return getSemesterID(self.term_start)

    def term_end_id(self):
      """
      Convert term_end semester string to numeric ID
      """
      return getSemesterID(self.term_end)

    def served_during_semester(self, semester_id):
      """
      Return True if this officer's term of office includes the given numeric
      semester ID, False otherwise
      """
      return self.term_start_id() <= semester_id <= self.term_end_id()

    def served_during_year(self, year):
      """
      Return True if this officer served during the given academic year, defined
      as Summer [year] to Spring [year + 1]; False otherwise
      """
      range_start_id = getSemesterID(f'SUMMER_{year}')
      range_end_id = getSemesterID(f'SPRING_{(year + 1)}')
      return self.term_start_id() < range_end_id and self.term_end_id() > range_start_id

    def is_current_student(self):
      # TODO
      pass

  class OfficersParams(Enum):
    """
    List of /api/officers query parameters
    """
    POSITION = 'position'
    SEMESTER = 'semester'
    YEAR = 'year'
    IS_CURRENT_STUDENT = 'is_current_student'

  def semesterIDType(reqstr):
    """
    Returns None if reqstr is not a semester string, and converts it to standard
    format if it is.
    Standard format is SEASON_YEAR, e.g. SPRING_2018
    TODO: accept more formats
    """
    template = re.compile(r'(SPRING|SUMMER|FALL)_\d\d\d\d')
    reqstr = str(reqstr).upper()
    if template.match(reqstr):
      return getSemesterID(reqstr)
    return None

  # Get officers from json file
  with open('officers.json') as officers_file:
    officers = json.load(officers_file, object_hook=Officer)

  # Filter by position (President etc.)
  position = request.args.get(OfficersParams.POSITION.value, default=None,
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
  year = request.args.get(OfficersParams.YEAR.value, default=None, type=int)

  if semester:
    officers = [x for x in officers if x.served_during_semester(semester)]
  elif not semester and OfficersParams.SEMESTER.value in request.args:
    # In this case, a semester parameter was passed but semesterStr failed to
    # match
    return jsonify({"error": "Invalid parameter 'semester'"}), 400
  elif year:
    # Filter by term academic year - semester param overrides this
    # We want all officers whose term began before the end, and ended after the
    # beginning, of this academic year.
    officers = [x for x in officers if x.served_during_year(year)]

  # TODO: Filter by current student status
  # if OfficersParams.IS_CURRENT_STUDENT.value in request.args:
  #   is_current_char = request.args.get(OfficersParams.IS_CURRENT_STUDENT.value, type=upperStr)
  #   if is_current_char in ('Y', 'T', 'YES', 'TRUE'):
  #     pass
  #   elif is_current_char in ('N', 'F', 'NO', 'FALSE'):
  #     pass
  #   else:
  #     return jsonify({"error": "Invalid parameter 'is_current'"}), 400

  # Convert Officer objects back to dictionaries before returning
  return jsonify([x.__dict__ for x in officers])


@app.route('/api/projects', methods=['GET'])
def getProjects():
    class Projects():
      """
      Represents Officer objects from the json file
      Used by json.load() - see 'object_hook' in the Python docs
      """
      def __init__(self, d):
        # d is the dictionary passed by json.load()
        self.name = str(d['name'])
        self.status = d['status']
        self.description = str(d['description'])
        self.smallImage = d['smallImage']
        self.largeImage = d['largeImage']
        self.wikiLink = d['wikiLink']
        self.githubLink = d['githubLink']
        self.startDate = d['startDate']
        self.projectLead = str(d['projectLead'])

    # Get projects from json file
    with open('projects.json') as projects_file:
      projects = json.load(projects_file, object_hook=Projects)

    # Convert project objects back to dictionaries before returning
    return jsonify([x.__dict__ for x in projects])
=======
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
  # NOTE: remember to update ordering in frontend project
  PRESIDENT = "PRESIDENT"
  VICE_PRESIDENT = "VICE_PRESIDENT"
  TREASURER = "TREASURER"
  SECRETARY = "SECRETARY"
  SENIOR_TECHNICAL_OFFICER = "SENIOR_TECHNICAL_OFFICER"
  TECHNICAL_OFFICER = "TECHNICAL_OFFICER"
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

@app.route('/api/officers', methods=['GET'])
def getOfficers():
  """
  API function to retrieve officers
  Parameters:
  /api/officers?position=[PRESIDENT,VICE_PRESIDENT,TREASURER,SECRETARY,TECHNICAL_OFFICER]
               ?semester=SEASON_YEAR
                  e.g. "?semester=SUMMER_2018
                  Overrides 'year'
               ?year=<Academic year>
                  e.g. "?year=2018" for Summer 2018 - Spring 2019 inclusive
                  Not read if 'semester' param exists
               ?is_current_student=[Y,N] - TODO
  """

  class Officer():
    """
    Represents Officer objects from the json file
    Used by json.load() - see 'object_hook' in the Python docs
    """
    def __init__(self, d):
      # d is the dictionary passed by json.load()
      self.name = str(d['name'])
      self.position = d['position']
      self.description = str(d['description'])
      self.github = d['github']
      self.slack = str(d['slack'])
      self.personal_site = d['personal_site']
      self.image = d['image']
      self.special_ability = str(d['special_ability'])
      self.join_date = d['join_date']
      self.term_start = d['term_start']
      self.term_end = d['term_end']
      self.graduating_semester = d['graduating_semester']

    def term_start_id(self):
      """
      Convert term_start semester string to numeric ID
      """
      return getSemesterID(self.term_start)

    def term_end_id(self):
      """
      Convert term_end semester string to numeric ID
      """
      return getSemesterID(self.term_end)

    def served_during_semester(self, semester_id):
      """
      Return True if this officer's term of office includes the given numeric
      semester ID, False otherwise
      """
      return self.term_start_id() <= semester_id <= self.term_end_id()

    def served_during_year(self, year):
      """
      Return True if this officer served during the given academic year, defined
      as Summer [year] to Spring [year + 1]; False otherwise
      """
      range_start_id = getSemesterID(f'SUMMER_{year}')
      range_end_id = getSemesterID(f'SPRING_{(year + 1)}')
      return self.term_start_id() < range_end_id and self.term_end_id() > range_start_id

    def is_current_student(self):
      # TODO
      pass

  class OfficersParams(Enum):
    """
    List of /api/officers query parameters
    """
    POSITION = 'position'
    SEMESTER = 'semester'
    YEAR = 'year'
    IS_CURRENT_STUDENT = 'is_current_student'

  def semesterIDType(reqstr):
    """
    Returns None if reqstr is not a semester string, and converts it to standard
    format if it is.
    Standard format is SEASON_YEAR, e.g. SPRING_2018
    TODO: accept more formats
    """
    template = re.compile(r'(SPRING|SUMMER|FALL)_\d\d\d\d')
    reqstr = str(reqstr).upper()
    if template.match(reqstr):
      return getSemesterID(reqstr)
    return None

  # Get officers from json file
  with open('officers.json') as officers_file:
    officers = json.load(officers_file, object_hook=Officer)

  # Filter by position (President etc.)
  position = request.args.get(OfficersParams.POSITION.value, default=None,
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
  year = request.args.get(OfficersParams.YEAR.value, default=None, type=int)

  if semester:
    officers = [x for x in officers if x.served_during_semester(semester)]
  elif not semester and OfficersParams.SEMESTER.value in request.args:
    # In this case, a semester parameter was passed but semesterStr failed to
    # match
    return jsonify({"error": "Invalid parameter 'semester'"}), 400
  elif year:
    # Filter by term academic year - semester param overrides this
    # We want all officers whose term began before the end, and ended after the
    # beginning, of this academic year.
    officers = [x for x in officers if x.served_during_year(year)]

  # TODO: Filter by current student status
  # if OfficersParams.IS_CURRENT_STUDENT.value in request.args:
  #   is_current_char = request.args.get(OfficersParams.IS_CURRENT_STUDENT.value, type=upperStr)
  #   if is_current_char in ('Y', 'T', 'YES', 'TRUE'):
  #     pass
  #   elif is_current_char in ('N', 'F', 'NO', 'FALSE'):
  #     pass
  #   else:
  #     return jsonify({"error": "Invalid parameter 'is_current'"}), 400

  # Convert Officer objects back to dictionaries before returning
  return jsonify([x.__dict__ for x in officers])
>>>>>>> 900f0b2407d6a81eefb3927296b59e4dfd4ff4ce
