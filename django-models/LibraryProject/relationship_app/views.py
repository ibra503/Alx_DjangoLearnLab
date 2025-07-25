from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view
class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'
