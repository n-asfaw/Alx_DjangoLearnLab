from django.shortcuts import render
from relationship_app.models import Book
from django.views.generic import DetailView
from relationship_app.models import Library


# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'list_books.html', {'books': books})


# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Template to render library details
    context_object_name = 'library'  # Name of the context variable used in the template
