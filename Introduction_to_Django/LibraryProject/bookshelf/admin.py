from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display
    list_filter = ('author', 'publication_year')  # Filter options
    search_fields = ('title', 'author')  # Search functionality

admin.site.register(Book, BookAdmin)
