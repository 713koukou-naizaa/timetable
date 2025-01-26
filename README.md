# Timetable
This Python script fetches and displays events from a given iCalendar file. It displays today's events and the next event of the day in a readable format.

## Features
- Fetches an iCalendar from a given URL or file
- Displays today's events
- Displays the next event of the day
- Saves the calendar to a file

## Requirements
- Python 3.x
- `requests` library
- `ics` library
- `datetime` library

## Installation
1. Clone the repository or download the script
    ```bash
    git clone https://github.com/713koukou-naizaa/timetable.git
    ```
2. Install the required libraries using pip:
    ```bash
    pip install requests ics datetime
    ```

## Usage
1. Update the url or filename used in the main function with your own url or filename
2. Run the script:
    ```bash
    python timetable.py
    ```

## Functions
- print_event_formatted(event): Print a given event in a readable format
- get_events_by_date(date, calendar): Print all events of a given date
- get_today_date(): Return today's date in the format `YYYY-MM-DD`
- get_next_event(calendar): Return the next upcoming event
- save_calendar_to_file(calendar, filename): Save a calendar object to a file
- display_next_event(calendar): Display the next event
- display_today_events(calendar): Display today's events
- fetch_calendar(url): Fetch the iCalendar file from the given URL
- create_calendar(url=None, filename=None): Create a calendar object from the given URL or filename