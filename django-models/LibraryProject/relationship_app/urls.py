# relationship_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # URL for the function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
]