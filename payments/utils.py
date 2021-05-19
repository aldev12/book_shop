import calendar
from datetime import datetime


def get_max_day_and_time(date: datetime) -> datetime:
    last_day = calendar.monthrange(date.year, date.month)[1]
    new_date = date.replace(day=last_day, hour=23, minute=59, second=59, microsecond=0)
    return new_date
