from dataclasses import dataclass


@dataclass
class LessonData:
    lesson_specific_date: str
    lesson_specific_start_time: str
    lesson_name: str
    lesson_type: str
    tutor_role: str
    tutor_initials: str
    swimming_pool: str
    swimming_time: str
    manufactory: str
    audience: str
    housing: str
