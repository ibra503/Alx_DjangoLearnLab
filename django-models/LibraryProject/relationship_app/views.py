from django.shortcuts import render
from .models import book
from django.views.generic import TemplateView
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
def Books_list(request):
    Books = Book.object.all()
    return (rende , 'list_books.html', {'books': books})


class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'libraries'

