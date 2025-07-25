from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure this line is included!

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

    def get_context_data(self, **kwargs):
        """
        Override the get_context_data method to add the list of books
        available in the library to the context.
        """
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book_set.all()  # Assuming a reverse relationship from Library to Book
        return context
