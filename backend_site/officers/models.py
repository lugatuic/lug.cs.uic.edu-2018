"""Data models representing the Officers record type"""

from enum import Enum


class OfficersParams(Enum):
    """List of /api/officers query parameters"""
    POSITION = 'position'
    SEMESTER = 'semester'
    YEAR = 'year'
    IS_CURRENT_STUDENT = 'is_current_student'


class Positions(Enum):
    """List of LUG Officer positions"""
    PRESIDENT = "PRESIDENT"
    VICE_PRESIDENT = "VICE_PRESIDENT"
    TREASURER = "TREASURER"
    SECRETARY = "SECRETARY"
    SENIOR_TECHNICAL_OFFICER = "SENIOR_TECHNICAL_OFFICER"
    TECHNICAL_OFFICER = "TECHNICAL_OFFICER"
    MEMBER = "MEMBER"


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
        Return True if this officer served during the given academic year,
        defined as Summer [year] to Spring [year + 1]; False otherwise
        """
        range_start_id = getSemesterID(f'SUMMER_{year}')
        range_end_id = getSemesterID(f'SPRING_{(year + 1)}')
        return (self.term_start_id() < range_end_id
                and self.term_end_id() > range_start_id)

    def is_current_student(self):
        """
        Return True if this student is currently enrolled; false otherwise
        """
        # TODO
        pass


def getSemesterID(semester_string):
    """
    Convert a semester string of the form "SEASON_YEAR" (e.g. "SPRING_2018")
    into a numeric value
    Works by left-shifting the year by 2 and adding a value for the season
    - fast, preserves ordering; can easily get season by testing modulo the
    season (e.g. if id % 4 == 1, season is Summer)
    """
    season, year_str = semester_string.strip().upper().split('_')
    if season == 'SPRING':
        season_id = 0
    elif season == 'SUMMER':
        season_id = 1
    elif season == 'FALL':
        season_id = 2
    else:  # Probably an error
        season_id = 3
    semester_id = (int(year_str) << 2) + season_id
    return semester_id
