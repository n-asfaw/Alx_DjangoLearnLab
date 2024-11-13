# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # Accessing related books through related_name='books'
    return books

# List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # Accessing related books through ManyToManyField
    return books

# Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Accessing related librarian through OneToOneField
    return librarian
