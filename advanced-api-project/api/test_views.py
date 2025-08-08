from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Book  # Optional, if you use it

class BookAPITests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('book-list')  # replace with your actual URL name

    def test_book_list_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # This line checks for 'response.data'
        self.assertIsNotNone(response.data)
        
self.client.login