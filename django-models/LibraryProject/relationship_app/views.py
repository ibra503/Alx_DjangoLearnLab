from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Author, Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    """
    Function-based view that lists all books stored in the database.
    This view should render a simple text list of book titles and their authors.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library, listing all books available
    in that library. This view should render a page that shows the library name and 
    all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Additional context can be added here if needed
        return context