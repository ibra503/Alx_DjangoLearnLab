from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library_list/', views.library_list, name='library_list'),

    # Class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
