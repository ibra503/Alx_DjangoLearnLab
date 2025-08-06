from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book
import datetime

class BookAPITests(APITestCase):
    """
    Test suite for Book API endpoints
    Uses separate test database automatically created by Django
    """
    
    def setUp(self):
        """Create test data and authenticated client"""
        # Create test users
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.admin = User.objects.create_superuser(
            username='admin',
            password='adminpassword'
        )
        
        # Create test authors
        self.author1 = Author.objects.create(name="J.R.R. Tolkien")
        self.author2 = Author.objects.create(name="George R.R. Martin")
        
        # Create test books
        self.book1 = Book.objects.create(
            title="The Hobbit",
            publication_year=1937,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title="A Game of Thrones",
            publication_year=1996,
            author=self.author2
        )
        
        # Configure authenticated clients
        self.client = APIClient()
        self.auth_client = APIClient()
        self.auth_client.force_authenticate(user=self.user)
        self.admin_client = APIClient()
        self.admin_client.force_authenticate(user=self.admin)
        
        # Current year for validation tests
        self.current_year = datetime.date.today().year

    def test_unauthenticated_access(self):
        """Test unauthenticated users have read-only access"""
        # List view
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Detail view
        response = self.client.get(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Create attempt
        response = self.client.post(reverse('book-list'), {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author1.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Update attempt
        response = self.client.put(reverse('book-detail', args=[self.book1.id]), {
            'title': 'Updated Title'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Delete attempt
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_book_creation(self):
        """Test authenticated users can create books with valid data"""
        data = {
            'title': 'The Two Towers',
            'publication_year': 1954,
            'author': self.author1.id
        }
        response = self.auth_client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'The Two Towers')

    def test_book_validation(self):
        """Test publication year validation rules"""
        # Future year should be rejected
        data = {
            'title': 'Future Book',
            'publication_year': self.current_year + 1,
            'author': self.author1.id
        }
        response = self.auth_client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Publication year cannot be in the future', str(response.data))
        
        # Past year should be accepted
        data['publication_year'] = 1999
        response = self.auth_client.post(reverse('book-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_update(self):
        """Test updating book details"""
        url = reverse('book-detail', args=[self.book1.id])
        data = {
            'title': 'The Hobbit: Revised Edition',
            'publication_year': 1951,
            'author': self.author1.id
        }
        response = self.auth_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'The Hobbit: Revised Edition')

    def test_book_deletion(self):
        """Test book deletion functionality"""
        initial_count = Book.objects.count()
        url = reverse('book-detail', args=[self.book2.id])
        
        # Regular user should not be able to delete
        response = self.auth_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), initial_count)
        
        # Admin should be able to delete
        response = self.admin_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), initial_count - 1)

    def test_filtering_by_publication_year(self):
        """Test filtering books by publication year"""
        # Create additional books for filtering
        Book.objects.create(
            title="The Fellowship of the Ring",
            publication_year=1954,
            author=self.author1
        )
        
        # Test year filter
        response = self.client.get(
            reverse('book-list'), 
            {'publication_year': 1954}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'The Fellowship of the Ring')

    def test_author_serialization(self):
        """Test author serialization includes nested books"""
        url = reverse('author-detail', args=[self.author1.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('books', response.data)
        self.assertEqual(len(response.data['books']), 1)
        self.assertEqual(response.data['books'][0]['title'], 'The Hobbit')
        
    def test_pagination(self):
        """Test API returns paginated results"""
        # Create additional books
        for i in range(15):
            Book.objects.create(
                title=f"Sample Book {i}",
                publication_year=2000 + i,
                author=self.author1
            )
        
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('count', response.data)
        self.assertIn('next', response.data)
        self.assertIn('previous', response.data)
        self.assertEqual(len(response.data['results']), 10)  # Default page size