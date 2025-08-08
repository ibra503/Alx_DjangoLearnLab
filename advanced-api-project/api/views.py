from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import status response.data
class BookListView(generics.ListCreateAPIView):
    """
    View for listing all books and creating new books
    Handles GET (list) and POST (create) methods
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Save the book with the current user as owner"""
        serializer.save()

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, or deleting a book instance
    Handles GET (retrieve), PUT (update), PATCH (partial update), DELETE
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'
    # Add to BookListView
def get_queryset(self):
    """Implement custom filtering"""
    queryset = super().get_queryset()
    
    # Filter by publication year if provided
    year = self.request.query_params.get('year')
    if year:
        queryset = queryset.filter(publication_year=year)
    
    return queryset

# Add to BookDetailView
def perform_update(self, serializer):
    """Custom update logic with validation"""
    instance = self.get_object()
    serializer.save()CreateView", "UpdateView", "DeleteView
    filters.OrderingFilter
    title, author
    filters.SearchFilter
    # Add this to BookListView for filtering support
from django_filters.rest_framework import DjangoFilterBackend

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['publication_year']
    pagination_class = PageNumberPagination  # Enable pagination for testing

class AuthorDetailView(generics.RetrieveAPIView):
    """View for author details with nested books"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer