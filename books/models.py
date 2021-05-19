from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
