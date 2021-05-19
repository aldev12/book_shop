from rest_framework.exceptions import ValidationError
from django.test import TestCase

from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentSerializerTest(TestCase):

    def test_can_not_create_payment_with_status_ok_and_without_period(self):
        """тест: нельзя создать платеж со статусом ok без заданного периода"""
        # Данные без параметра period
        data = {'user': 1, 'status': Payment.STATUS_OK}

        # Хотим видеть что во время проверки данных поднимется исключение
        with self.assertRaises(ValidationError):
            PaymentSerializer().validate(data)

    def test_can_not_create_payment_with_status_error_and_without_msg(self):
        """тест: нельзя создать платеж со статусом error без заданного сообщения"""
        # Данные без параметра msg
        data = {'user': 1, 'status': Payment.STATUS_ERROR}

        # Хотим видеть что во время проверки данных поднимется исключение
        with self.assertRaises(ValidationError):
            PaymentSerializer().validate(data)
