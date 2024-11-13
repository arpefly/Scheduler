import os.path
from datetime import date, time, timedelta, datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dataclass.lesson_data import LessonData


class CalendarWorker:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/calendar']
        self.creds = None

        if os.path.exists('creds/token.json'):
            self.creds = Credentials.from_authorized_user_file('creds/token.json', self.scopes)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('creds/credentials.json', self.scopes)
                creds = flow.run_local_server(port=1564)

            with open('creds/token.json', 'w') as token:
                token.write(self.creds.to_json())

        try:
            self.service = build('calendar', 'v3', credentials=self.creds)
        except HttpError as ex:
            print(f'An HTTP error occurred: {ex}')

    def insert_lesson_event(self, calendar_id: str, lesson_data: LessonData, start_time: time, lesson_date: date, until: str, interval: int):
        if lesson_data.swimming_pool is None and lesson_data.manufactory is None:
            if lesson_data.housing is not None:
                if lesson_data.housing.strip() == 'гл.':
                    lesson_data.housing = 'гл.к.'
                lesson_data.housing = lesson_data.housing.replace('.', '. ').strip()

            location = f'{lesson_data.housing}, ауд. {lesson_data.audience}'
        elif lesson_data.swimming_pool is not None:
            if lesson_data.swimming_time is not None:
                start_time = datetime.strptime(lesson_data.swimming_time, '%H:%M').time()
            location = 'Бассейн'
        elif lesson_data.manufactory is not None:
            location = lesson_data.manufactory
        else:
            location = ' '


        start_time = start_time if lesson_data.lesson_specific_start_time is None else datetime.strptime(lesson_data.lesson_specific_start_time, '%H:%M').time()
        temp_time = datetime.combine(datetime.now().date(), start_time) + timedelta(hours=1.5)
        end_time = time(temp_time.hour, temp_time.minute)

        if lesson_data.lesson_specific_date is not None:
            lesson_date = datetime.strptime(lesson_data.lesson_specific_date, '%d.%m')
            lesson_date = date(datetime.now().year, lesson_date.month, lesson_date.day)
            rrule = f'RRULE:FREQ=DAILY;COUNT=1'
        else:
            rrule = f'RRULE:FREQ=WEEKLY;UNTIL={until};INTERVAL={interval}'

        event = {
            'summary': f'{lesson_data.lesson_name.lower().strip()} {lesson_data.lesson_type.strip()}',
            'location': location,
            'description': f'{lesson_data.tutor_role.strip()} {lesson_data.tutor_initials.strip()}',
            'start': {
                'dateTime': f'{lesson_date}T{start_time}+05:00',
                'timeZone': 'Asia/Yekaterinburg',
            },
            'end': {
                'dateTime': f'{lesson_date}T{end_time}+05:00',
                'timeZone': 'Asia/Yekaterinburg',
            },
            'recurrence': [
                rrule
            ]
        }

        self.service.events().insert(
            calendarId=calendar_id,
            body=event).execute()

    def get_calendars_list(self) -> dict:
        calendars = {}

        calendar_list = self.service.calendarList().list(pageToken=None).execute()
        for item in calendar_list['items']:
            calendars[item['id']] = item['summary']


        return calendars
