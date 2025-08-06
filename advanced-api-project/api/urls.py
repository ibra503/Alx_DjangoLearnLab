from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    "books/create", "books/update", "books/delete"
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]