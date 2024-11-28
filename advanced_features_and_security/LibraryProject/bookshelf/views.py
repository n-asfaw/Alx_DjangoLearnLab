
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import BookSearchForm

# Create your views here.
def home(request):
    return render(request, 'bookshelf/home.html')  # Render the home.html template

def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
        return render(request, 'bookshelf/book_list.html', {'books': books})
    return render(request, 'bookshelf/book_list.html', {'form': form})

# View for creating a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        Book.objects.create(title=title, author=author, publication_date=publication_date)
        return redirect('book_list')
    return render(request, 'create_book.html')

# View for editing a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_date = request.POST.get('publication_date')
        book.save()
        return redirect('book_detail', book_id=book.id)
    return render(request, 'edit_book.html', {'book': book})

# View for viewing a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

# View for deleting a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')    