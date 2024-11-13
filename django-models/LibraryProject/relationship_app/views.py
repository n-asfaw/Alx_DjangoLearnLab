# relationship_app/views.py

from django.shortcuts import render
from relationship_app.models import Book

def list_books(request):
    # Fetch all books from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template and pass the books
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from relationship_app.models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Path to your template
    context_object_name = 'library'  # This will be used in the template to refer to the object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can add any additional context here, like books in the library
        context['books'] = self.object.books.all()  # All books related to the library
        return context