from django.urls import path
from . import views

urlpatterns = [
    path("book_list/", views.Books_list, name="book_list"),  # function-based view
    path("library_list/", views.LibraryListView.as_view(), name="library_list"),  # class-based view
]
