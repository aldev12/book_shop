from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.utils import timezone

from books.models import Book
from books.viewsets import BookViewSet
from payments.models import Payment


class BookViewSetTest(TestCase):

    def create_user(self, with_login=False):
        username = 'test_user'
        user_pwd = 'test_password'
        user = User.objects.create_user(username, 'test_user@mail.ru', user_pwd)

        if with_login:
            self.client.login(username=username, password=user_pwd)

        return user

    def create_book(self):
        book = Book.objects.create(author='test author', content='i am book')

        return book

    def test_allow_only_get_and_post(self):
        """тест: разрешены только методы get и post """
        self.assertEqual(BookViewSet.http_method_names, ['get', 'post'])

    def test_can_get_list_books_with_authenticated(self):
        """тест: авторизованный пользователь может получить список книг"""
        # Создаем пользователя и авторизовываемся им
        self.create_user(with_login=True)

        # Запрашиваем список книг
        response = self.client.get(f'/api/books/')

        # Хотим видеть что запрос прошел успешно
        self.assertEqual(response.status_code, 200)

    def test_can_not_get_list_books_without_authenticated(self):
        """тест: не авторизованный пользователь не имеет доступа к списку книг"""

        # Запрашиваем список книг
        response = self.client.get(f'/api/books/')

        # Хотим видеть что нет доступа
        self.assertEqual(response.status_code, 403)

    @override_settings(TRIAL_PERIOD={'days': 1})
    def test_can_get_book_with_authenticated_with_tria_period(self):
        """тест: авторизованный пользователь может получить содержимое книги в пробный период"""
        # Создаем пользователя и авторизовываемся им
        self.create_user(with_login=True)

        # Создаем книгу, которую будем просматривать
        book = self.create_book()

        # Запрашиваем список книг
        response = self.client.get(f'/api/books/{book.pk}/')

        # Хотим видеть что запрос прошел успешно
        self.assertEqual(response.status_code, 200)

    @override_settings(TRIAL_PERIOD={'days': 0})
    def test_can_get_book_with_authenticated_with_payment(self):
        """тест: авторизованный пользователь может получить содержимое книги после оплаты"""
        # Создаем пользователя и авторизовываемся им
        user = self.create_user(with_login=True)

        # Создаем оплату за текущий месяц, т.е. подписка у мользователя будет активна на текущий месяц
        Payment.objects.create(user=user, period=timezone.now(), status=Payment.STATUS_OK)

        # Создаем книгу, которую будем просматривать
        book = self.create_book()

        # Запрашиваем содержимое книги
        response = self.client.get(f'/api/books/{book.pk}/')

        # Хотим видеть что запрос прошел успешно
        self.assertEqual(response.status_code, 200)

    def test_can_not_get_book_without_authenticated(self):
        """тест: не авторизованный пользователь не имеет доступа к содержанию книг"""

        # Создаем книгу, которую будем просматривать
        book = self.create_book()

        # Запрашиваем содержимое книги
        response = self.client.get(f'/api/books/{book.pk}/')

        # Хотим видеть что нет доступа
        self.assertEqual(response.status_code, 403)
