# Import the models
from relationship_app.models import Author, Book, Library, Librarian

# --------------------------------------------
# 1️⃣ Query all books by a specific author
# --------------------------------------------
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")

# --------------------------------------------
# 2️⃣ List all books in a library
# --------------------------------------------
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()  # ManyToMany field
    print(f"\nBooks in {library_name}:")
    for book in library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# --------------------------------------------
# 3️⃣ Retrieve the librarian for a library
# --------------------------------------------
try:
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
