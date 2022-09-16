from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book, SavedBook, MarkUp

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('url', 'id', 'title', 'author', 'publication_date', 'featured')


class SavedBookSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True) #show name instead of pk
    book = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = SavedBook
        fields = ('url', 'id', 'user', 'book', 'status')

class MarkUpSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(slug_field="title", read_only=True)

    class Meta:
        model = MarkUp
        fields = ('url', 'id', 'user', 'book', 'page_number', 'note', 'created_at,', 'public')