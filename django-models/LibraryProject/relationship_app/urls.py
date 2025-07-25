from django.urls import path
from . import views

# Define the app namespace (optional but recommended)
app_name = 'relationship_app'

urlpatterns = [
    # Function-based view URL pattern
    path('books/', views.list_books, name='list_books'),
    
    # Class-based view URL pattern
    # <int:pk> captures the library ID from the URL
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]