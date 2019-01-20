"""Data models representing the Events record type"""

from datetime import datetime, timedelta
from icalendar import Calendar
import requests  # using this to yank the ics file from google calendar

CALURL = 'https://calendar.google.com/calendar/ical/ca149os3pmnh0dcopr1jn2negg%40group.calendar.google.com/public/basic.ics'
DTSTRFORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

EV = []
EVENTS_CACHED = datetime.now()


def getCacheEvents():
    """
    Return events from cache or internet as appropriate
    """
    if (EV == []) or (datetime.now() - EVENTS_CACHED >= timedelta(hours=1)):
        cacheEvents()
    return EV


def convertEvent(comp):
    """
    Convert an event in icalendar's dictionary-like format into our api
    format
    """
    today = datetime.today()
    endtime = comp.decoded('DTEND')
    compday = datetime(endtime.year, endtime.month, endtime.day)
    if today <= compday:
        # TODO: What if the start or end time is missing?
        return {
            'summary':     comp.decoded('SUMMARY', default=b'UNKNOWN EVENT')
                           .decode('UTF-8'),
            'timeStart':   comp.decoded('DTSTART')
                           .strftime(DTSTRFORMAT),
            'timeEnd':     endtime.strftime(DTSTRFORMAT),
            'location':    comp.decoded('LOCATION', default=b'')
                           .decode('UTF-8'),
            'description': comp.decoded('DESCRIPTION', default=b'')
                           .decode('UTF-8')
        }
    return None


def cacheEvents():
    """Caches the event calendar."""
    global EV, EVENTS_CACHED

    cal_request = requests.get(CALURL)
    cal_request.raise_for_status()  # Catch this exception in the view

    gcal = Calendar.from_ical(cal_request.content)
    events = [convertEvent(x) for x in gcal.walk(name="VEVENT")]
    EV = [x for x in events if x]
    EVENTS_CACHED = datetime.now()
