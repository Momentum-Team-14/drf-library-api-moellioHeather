from rest_framework import generics, status
from .models import Book, SavedBook, MarkUp
from .serializers import BookSerializer, SavedBookSerializer, MarkUpSerializer
from rest_framework.decorators import action
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from django.shortcuts import get_object_or_404

# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author']

    # def duplicate_book_entry(self):
    #     return super().create(request, *args, **kwargs)
    #     except IntegrityError:
    #     error_data = {
    #         "error": "Unique constraint violation: a title with this author already exists."}
    #     return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def perform_create(self, serializer):
    #     book = get_object_or_404(
    #         Book, pk=self.kwargs.get("pk"))
    #     serializer.save(book=book)


class SavedBookList(generics.ListCreateAPIView):
    queryset = SavedBook.objects.all()
    serializer_class = SavedBookSerializer

    def get_queryset(self):
        queryset = self.request.user.saved.all()
        return queryset

    # lookup book to save/add notes to
    # save status with book

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user=self.request.user.id).order_by('book')


class SaveBookView(CreateAPIView):
    queryset = SavedBook.objects.all()
    serializer_class = SavedBookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        breakpoint
        pass
    #     book = get_object_or_404(
    #         Book, pk=self.kwargs.get("pk"))
    #     serializer.save(book=book)


class MarkUpList(generics.ListCreateAPIView):
    queryset = MarkUp.objects.all()
    serializer_class = MarkUpSerializer


class MarkUpBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarkUp.objects.all()
    serializer_class = MarkUpSerializer

    # def perform_create(self, serializer):
    #     book = get_object_or_404(
    #         Book, pk=self.kwargs.get("pk"))
    #     serializer.save(book=book)


@api_view(['GET'])  # new
def api_root(request, format=None):
    return Response({
        'all-books': reverse('all-books', request=request, format=format),
        'saved-books': reverse('saved-books', request=request, format=format),
        'markup-list': reverse('markup-list', request=request, format=format),
    })
