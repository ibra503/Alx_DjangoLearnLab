from django.urls import path
from . import views

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),  # Function-based view
    path('library_list/', views.LibraryListView.as_view(), name='library_list'),  # Class-based view
]
