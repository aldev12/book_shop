from datetime import timedelta

from django.conf import settings
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from books.models import Book
from books.serializers import BookPartialSerializer, BookFullSerializer
from payments.models import Payment


class IsAllowedAccessBooks(BasePermission):
    def has_permission(self, request, view):
        is_trial_period = request.user.date_joined > timezone.now() - timedelta(**settings.TRIAL_PERIOD)
        is_allowed_access = Payment.objects.filter(user=request.user, period__gte=timezone.now()).exists()
        return bool(is_trial_period or is_allowed_access)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookPartialSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsAllowedAccessBooks]
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = BookFullSerializer
        return super().retrieve(request, *args, **kwargs)
