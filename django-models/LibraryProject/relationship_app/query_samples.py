# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def books_by_author(author_name):
    try:
        # Get the author by name
        author = Author.objects.get(name=author_name)
        # Get all books by the author
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return f"No author found with the name {author_name}"

# Query 2: Get all books in a library
def books_in_library(library_name):
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        # Get all books in the library
        books = library.books.all()  # ManyToManyField gives us all related books
        return books
    except Library.DoesNotExist:
        return f"No library found with the name {library_name}"

# Query 3: Get the librarian for a specific library
def librarian_for_library(library_name):
    try:
        # Get the library by name
        library = Library.objects.get(name=library_name)
        # Get the librarian for the library (OneToOneField gives one related object)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return f"No library found with the name {library_name}"
    except Librarian.DoesNotExist:
        return f"No librarian assigned to the library {library_name}"
