from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from payments.models import Payment
from payments.utils import get_max_day_and_time


class PaymentTest(TestCase):

    def test_check_period_after_create(self):
        """тест: проверяем период в платеже после создания"""
        date = timezone.now()

        # Получаем дату с максимальным временем и днем месяца
        max_date = get_max_day_and_time(date)

        # Создаем пользователя, у которого будет подписка
        user = User.objects.create(username='test_user')

        # Создаем платеж c текущей датой и временем
        payment = Payment.objects.create(user=user, period=date, status=Payment.STATUS_OK)

        # Хотим видеть что пользователь и период у платежа верные
        self.assertEqual(payment.user, user)
        self.assertEqual(payment.period, max_date)
