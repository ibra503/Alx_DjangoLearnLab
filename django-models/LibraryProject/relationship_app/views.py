from django.shortcuts import render
from .models import book
from django.views.generic import TemplateView

from django.views.generic.detail import DetailView
def Books_list(request):
    Books = Book.object.all()
    return (rende , 'list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
