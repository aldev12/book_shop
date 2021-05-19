import datetime
from unittest import TestCase

from payments.utils import get_max_day_and_time


class UtilDateTimeMethodsTest(TestCase):

    def test_get_max_day_and_time(self):
        """тест: получаем максимальный день и время даты"""

        # Задаем дату (берем високосный год и месяц февраль)
        test_date = datetime.datetime(day=1, month=2, year=2020)
        max_test_date = test_date.replace(day=29, hour=23, minute=59, second=59)

        max_date = get_max_day_and_time(test_date)

        # Хотим видеть что получили максимальную дату и время
        self.assertEqual(max_test_date, max_date)
