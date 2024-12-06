from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List and create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create
    # Update an existing book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  
    # Delete a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  
]
