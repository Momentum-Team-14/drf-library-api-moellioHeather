from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'author', 'publication_date', 'genre', 'featured')

# class UserSerializer(serializers.Serializer):
#     book = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())

#     class Meta:
#         model = User
#         fields - ('id', 'username', 'book')
