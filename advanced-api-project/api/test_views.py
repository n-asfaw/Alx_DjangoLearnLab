from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an author instance
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a user to authenticate
        self.user = User.objects.create_user(username="testuser", password="password")
        
        # Book data
        self.book_data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 1997,
            "author": self.author.id,
        }
        
        self.book = Book.objects.create(**self.book_data)
    
    def test_create_book(self):
        # Authenticate
        self.client.login(username="testuser", password="password")
        
        # Send POST request to create a book
        response = self.client.post('/api/books/', self.book_data, format='json')
        
        # Assert successful creation (status 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
    
    def test_get_books_list(self):
        # Get the list of books
        response = self.client.get('/api/books/')
        
        # Assert the list response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)  # Should contain at least one book
    
    def test_update_book(self):
        # Update book data
        updated_data = {
            "title": "Harry Potter and the Chamber of Secrets",
            "publication_year": 1998,
        }
        
        # Authenticate
        self.client.login(username="testuser", password="password")
        
        # Send PUT request to update the book
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
        
        # Assert the update was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_data['title'])
    
    def test_delete_book(self):
        # Authenticate
        self.client.login(username="testuser", password="password")
        
        # Send DELETE request to delete the book
        response = self.client.delete(f'/api/books/{self.book.id}/')
        
        # Assert successful deletion (status 204 No Content)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Check if the book is really deleted from the database
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())
    
    def test_filter_books_by_title(self):
        # Filter books by title
        response = self.client.get('/api/books/?title=Harry Potter')
        
        # Assert filtering works
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_search_books(self):
        # Search books by title
        response = self.client.get('/api/books/?search=Harry')
        
        # Assert searching works
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)
    
    def test_order_books_by_publication_year(self):
        # Order books by publication year
        response = self.client.get('/api/books/?ordering=publication_year')
        
        # Assert ordering works
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_unauthenticated_user_permission(self):
        # Test that an unauthenticated user cannot create, update, or delete books
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        response = self.client.put(f'/api/books/{self.book.id}/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
