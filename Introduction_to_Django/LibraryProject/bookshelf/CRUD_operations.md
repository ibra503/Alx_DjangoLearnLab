# All CRUD Commands

## Create
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Retrieve
>>> book = Book.objects.get(title="1984")
>>> book.title
>>> book.author
>>> book.publication_year

## Update
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

## Delete
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> Book.objects.all()

