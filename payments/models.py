from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from payments.utils import get_max_day_and_time


class Payment(models.Model):

    STATUS_OK = 'ok'
    STATUS_ERROR = 'error'
    STATUS_CHOICE = (
        (STATUS_OK, 'Ok'),
        (STATUS_ERROR, 'Error'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    period = models.DateTimeField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if period := self.period:
            self.period = get_max_day_and_time(period)
        super().save(force_insert, force_update, using, update_fields)
