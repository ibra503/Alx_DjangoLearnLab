from django.http import Httprequest


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]