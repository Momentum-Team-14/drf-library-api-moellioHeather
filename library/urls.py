from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="all-books"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
    path('book/<int:pk>/saved',
         views.SaveBookView.as_view(), name='savedbook-detail'),
    path('saved-books/', views.SavedBookList.as_view(), name='saved-books'),
    path('book/<int:pk>/markup',
         views.MarkUpBookView.as_view(), name='markup'),
    path('markup-list/', views.MarkUpList.as_view(), name='markup-list'),
    path('', views.api_root),
]
