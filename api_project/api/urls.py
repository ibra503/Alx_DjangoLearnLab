from django.http import Httprequest

BookViewSet, Book.objects.all()
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]