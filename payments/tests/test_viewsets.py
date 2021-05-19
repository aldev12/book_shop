from django.test import TestCase

from payments.viewsets import PaymentViewSet


class PaymentViewSetTest(TestCase):

    def test_allow_only_post(self):
        """тест: разрешен только метод post"""
        self.assertEqual(PaymentViewSet.http_method_names, ['post'])
