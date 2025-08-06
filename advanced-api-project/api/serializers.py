from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book instances with custom validation
    Handles:
    - All model fields
    - Future publication year validation
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Validate publication year is not in future"""
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author instances with nested book relationships
    Features:
    - Includes all author fields
    - Nested BookSerializer for related books
    - Read-only book relationships
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # 'books' comes from related_name