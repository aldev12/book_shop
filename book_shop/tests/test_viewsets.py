from django.test import TestCase

from book_shop.viewsets import UserViewSet


class UserViewSetTest(TestCase):

    def test_allow_only_get_and_post(self):
        """тест: разрешены только методы get и post"""
        self.assertEqual(UserViewSet.http_method_names, ['get', 'post'])
