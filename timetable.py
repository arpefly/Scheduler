import re
from datetime import datetime, time, date, timedelta

from openpyxl import load_workbook

from calendar_api import CalendarWorker
from dataclass.lesson_data import LessonData


class TimeTable:
    def __init__(self, time_table_path):
        self.timetable_path = time_table_path
        self.workbook = load_workbook(self.timetable_path)
        self.sheet = self.workbook.active
        self.months_dict = {
            'января': 1,
            'февраля': 2,
            'марта': 3,
            'апреля': 4,
            'мая': 5,
            'июня': 6,
            'июля': 7,
            'августа': 8,
            'сентября': 9,
            'октября': 10,
            'ноября': 11,
            'декабря': 12
        }
        self.start_time = {
            1: time(hour=8),
            2: time(hour=9, minute=40),
            3: time(hour=11, minute=30),
            4: time(hour=13, minute=20),
            5: time(hour=15),
            6: time(hour=16, minute=40)
        }

    def get_start_date(self,) -> date:
        commons = self.sheet['a2'].value.split()
        day = int(commons[3])
        month = self.months_dict[commons[4].lower()]
        start_date = date(datetime.now().year, month, day)
        return start_date

    def get_week_parity(self) -> int:
        return int(self.sheet['a2'].value.split()[-2])

    def parse_timetable(self, push: bool, until: str, calendar_id: str, calendar_worker: CalendarWorker | None) -> ([], []):
        regex = r'(?P<lesson_specific_date>\d{1,2}\.\d{1,2})? ?(?P<lesson_specific_start_time>\d{1,2}:\d{1,2})? ?(?P<lesson_name>[A-ZА-ЯЁ,\- ]+) (?P<lesson_type>\(пр\)|\(лек\)|\(лаб\)) ?(?P<tutor_role>пр\.|асс\.|ст\. пр\.|доц\.|проф.)? ?(?P<tutor_initials>[А-ЯЁ][а-яё]+ [А-ЯЁ]\.[А-ЯЁ]\.)? ?(?P<swimming_time>\d{1,2}:\d{1,2})? ?(?P<swimming_pool>Бассейн)? ?(?P<manufactory>ПНППК)? ?(?P<audience>\d+[а-яё]*)? ?(?P<housing>\гл\.к\. ?|гл\. ?|к\. ?[АБВГД])?'
        lesson_num = 0
        i = 4
        current_date = self.get_start_date()
        week_parity = self.get_week_parity()

        first_week = []
        second_week = []

        while i <= 75:
            lesson_str = self.sheet[f'C{i}'].value
            lesson_str = '---' if lesson_str is None else (
                lesson_str.replace('\n', ' ').replace(' ', ' ').replace('  ', ' '))

            matches = re.search(regex, lesson_str)
            lesson_data = None
            if matches is not None:
                lesson_data = LessonData(**matches.groupdict())

                aud = f', ауд. {lesson_data.audience}' if lesson_data.housing is not None else ''
                cell_info = ((f'{lesson_data.lesson_specific_start_time or lesson_data.swimming_time or ''} '
                              f'{lesson_data.lesson_specific_date or ''} '
                              f'{lesson_data.lesson_name.title()}\n'
                              f'{lesson_data.tutor_role} {lesson_data.tutor_initials}\n'
                              f'{lesson_data.housing or lesson_data.swimming_pool or lesson_data.manufactory or ''}{aud}')
                             .strip().replace('  ', ' '))

            if self.is_cell_merged(f'C{i}'):
                if lesson_data:
                    first_week.append(cell_info)
                    second_week.append(cell_info)

                    if push:
                        calendar_worker.insert_lesson_event(calendar_id=calendar_id,
                                                            lesson_data=LessonData(**matches.groupdict()),
                                                            start_time=self.start_time[lesson_num % 6 + 1],
                                                            lesson_date=current_date,
                                                            until=until,
                                                            interval=1)
                else:
                    first_week.append('')
                    second_week.append('')
                i += 1
            else:
                if lesson_data:
                    if push:
                        calendar_worker.insert_lesson_event(calendar_id=calendar_id,
                                                            lesson_data=LessonData(**matches.groupdict()),
                                                            start_time=self.start_time[lesson_num % 6 + 1],
                                                            lesson_date=current_date + timedelta(days=7 if i % 2 == week_parity % 2 else 0),
                                                            until=until,
                                                            interval=2)
                    if i % 2 == 0:
                        first_week.append(cell_info)
                    else:
                        second_week.append(cell_info)
                else:
                    if i % 2 == 0:
                        first_week.append('')
                    else:
                        second_week.append('')

            i += 1
            if i % 2 == 0:
                lesson_num += 1
            if (i - 4) % 12 == 0:
                current_date += timedelta(days=1)

        return first_week, second_week

    def is_cell_merged(self, cell_to_check: str) -> bool:
        for merged_range in self.sheet.merged_cells.ranges:
            if cell_to_check in merged_range:
                min_col, min_row, max_col, max_row = merged_range.bounds
                if min_col == max_col or min_col + min_row + 2 == max_col + max_row:
                    return True
        return False
