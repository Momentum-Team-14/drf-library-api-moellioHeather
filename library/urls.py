from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('saved-books/', views.SavedBookList.as_view(), name='saved-books'),
    path('saved/<int:pk>', views.SavedBookDetail.as_view(), name='savedbook-detail'),
    path('markups/', views.MarkUpList.as_view(), name='markup-list'),
    path('markup-detail/<int:pk>', views.MarkUpDetail.as_view(), name='markup-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
