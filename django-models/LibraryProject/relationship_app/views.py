from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Make sure this line is included!

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that displays all books in the database.
    Renders a list of book titles and their authors.
    """
    books = Book.objects.all()  # Get all books from database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library.
    Shows the library name and all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
