from rest_framework import serializers
from .models import Author, Book

# Book serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
    
    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Author serializer with a nested BookSerializer
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
