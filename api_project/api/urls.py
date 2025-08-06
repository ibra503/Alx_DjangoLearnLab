from django.http import Httprequest

DefaultRouter() router.urls include
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]