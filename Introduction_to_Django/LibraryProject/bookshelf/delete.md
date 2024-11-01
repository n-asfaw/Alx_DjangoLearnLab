# Delete Operation

**Command:**
```python
from bookshelf.models import Book  # Import the Book model

book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book instance
book.delete()  # Delete the book instance
books = Book.objects.all()  # Confirm deletion
print(books)  # Print remaining books
