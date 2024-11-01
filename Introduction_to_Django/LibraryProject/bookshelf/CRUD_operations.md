# CRUD Operations Documentation

## Create

**Command:**


book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()




retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)


book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)


book.delete()
books = Book.objects.all()
print(books)
