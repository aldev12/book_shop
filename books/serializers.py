from rest_framework import serializers

from books.models import Book


class BookPartialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['author']


class BookFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['author', 'content']