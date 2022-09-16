from rest_framework import generics
from .models import Book, SavedBook, MarkUp
from .serializers import BookSerializer, SavedBookSerializer, MarkUpSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def get_serializer_class(self):
    #     if self.action in ['list', 'favorite']:
    #         return 
    #     return super().get_serializer_class()

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class SavedBookList(generics.ListCreateAPIView):
    queryset = SavedBook.objects.all()
    serializer_class = SavedBookSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user.id).order_by('book')

class SavedBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedBook.objects.all()
    serializer_class = SavedBookSerializer

class MarkUpList(generics.ListCreateAPIView):
    queryset = MarkUp.objects.all()
    serializer_class = MarkUpSerializer


class MarkUpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarkUp.objects.all()
    serializer_class = MarkUpSerializer

@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
        'saved-books': reverse('saved-books', request=request, format=format),
        'markups': reverse('markup-list', request=request, format=format),
    })










