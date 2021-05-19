from rest_framework import routers

from book_shop.viewsets import UserViewSet
from books.viewsets import BookViewSet
from payments.viewsets import PaymentViewSet

router = routers.DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'users', UserViewSet)