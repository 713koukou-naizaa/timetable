"""
Timetable Script

This script fetches and displays events from a given iCalendar file or URL. It displays today's events and the next event of the day in a readable format.

Author: 713koukou-naizaa
Contact: nzo.akt@gmail.com
Date: 2025-01-26
"""

import requests
import os
from ics import Calendar
from datetime import datetime
from dotenv import load_dotenv


def print_event_formatted(event):
    """
    print a given event in a readable format
    
    :param event: event object (ics.Event)
    :return: None
    """
    
    print("name: {}".format(event.name))
    print("day: {} ({})".format(event.begin.strftime("%A"), event.begin.strftime("%d")))
    print("time: {} - {}".format(event.begin.time(), event.end.time()))
    print("location: {}".format(event.location))
    print("description: {}".format(" ".join(event.description.splitlines())))
    print("------------------")

def get_events_by_date(date, calendar):
    """
    print all events of a given date
    
    :param day: string of given date with format "YYYY-MM-DD"
    :param calendar: calendar object (ics.Calendar)
    :return: none
    """
    date = datetime.strptime(date, "%Y-%m-%d").date()
    events_found = False
    for event in calendar.events:
        if event.begin.date() == date:
            print_event_formatted(event)
            events_found = True
    if not events_found:
        print("No events for day: {} ({})".format(date.strftime("%A"), date.strftime("%d")))

def get_today_date():
    """
    return today's date with format YYYY-MM-DD
    
    :return: string
    """
    return datetime.today().strftime("%Y-%m-%d")

from datetime import datetime, timezone

def get_next_event(calendar):
    """
    return the next event
    
    :param calendar: calendar object (ics.Calendar)
    :return: ics.Event
    """
    now = datetime.now(timezone.utc)
    for event in calendar.timeline:
        if event.begin > now:
            return event
    return None

def save_calendar_to_file(calendar, filename):
    """
    save calendar to file
    
    :param calendar: calendar object (ics.Calendar)
    :param filename: filename to save calendar to
    :return: None
    """
    with open(filename, "w") as f:
        f.writelines(calendar)
        print("calendar saved successfully")

def display_next_event(calendar):
    """
    display next event
    
    :param calendar: calendar object (ics.Calendar)
    :return: None
    """
    
    next_event = get_next_event(calendar=calendar)
    print("next event:")
    print_event_formatted(event=next_event)

def display_today_events(calendar):
    """
    display today's events
    
    :param calendar: calendar object (ics.Calendar)
    :return: None
    """
    
    print("today's events:")
    get_events_by_date(date=get_today_date(), calendar=calendar)

def fetch_calendar(url):
    """
    fetch ical file from given url
    
    :param url: url of the ical file (ie. https://website.com/timetable/exportlink)
    :return: response object (requests.Response)
    """
    response = requests.get(url)
    return response

def construct_calendar_url(base_url, variable_part):
    """
    construct ical file url from given base url and variable part
    
    :param base_url: base url of the ical file (ie. https://website.com/timetable/)
    :param variable_part: variable part of the ical file (ie. exportlink)
    :return: url of the ical file (ie. https://website.com/timetable/exportlink)
    """
    return base_url + variable_part

def create_calendar(url=None, filename=None):
    """
    create calendar object from given url or given filename
    
    :param url: export url ical file (https://website.com/timetable/exportlink)
    :param filename: filename of ical file
    :return: calendar object (ics.Calendar) or None if error
    """
    
    if url:
        response = fetch_calendar(url)
        if response.status_code == 200:
            calendar = Calendar(response.text)
            print("calendar loaded successfully")
        else:
            calendar = None
            print("error loading calendar (status code: {})".format(response.status_code))
    elif filename:
        with open(filename, "r") as f:
            calendar = Calendar(f.read())
        print("calendar read successfully")
    else:
        print("error creating calendar: no url or filename given")
        return None

    return calendar
    

def main():
    """
    main function to create and manage calendar events

    create calendar object from given URL or file,
    save calendar to file, and display next upcoming event
    and today's events in readable format
    
    :return: None
    """
    
    load_dotenv()

    url=construct_calendar_url(base_url=os.getenv("BASE_URL"), variable_part=os.getenv("VARIABLE_PART"))

    calendar=create_calendar(url=url, filename="calendar.ics")

    if calendar is None:
        print("error creating calendar")
        return

    save_calendar_to_file(calendar, "calendar.ics")
    
    display_next_event(calendar)
    display_today_events(calendar)


if __name__ == "__main__":
    main()