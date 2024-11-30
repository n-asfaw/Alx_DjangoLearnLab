from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieves all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to convert model data to JSON

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # The list of all books in the database
    serializer_class = BookSerializer  # Serializer used to convert Book instances to JSON