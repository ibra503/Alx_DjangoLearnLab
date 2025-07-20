import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "relationship_app.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print("Books by John Doe:", books_by_author)


library = Library.objects.get(name="liberary_name")
books_in_library = library.books.all()
print("Books in Central Library:", books_in_library)


librarian = Librarian.objects.get(library=library)
print("Librarian:", librarian)

