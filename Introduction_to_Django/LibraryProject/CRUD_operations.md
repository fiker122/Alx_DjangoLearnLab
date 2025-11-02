# CRUD Operations for Book Model

## Create

```python
from bookshelf.models import Book

# Create a book
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book1  # <Book: 1984 by George Orwell (1949)>
# Retrieve all books
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve the book
book1 = Book.objects.get(title="1984")

# Update title
book1.title = "Nineteen Eighty-Four"
book1.save()

# Confirm update
Book.objects.all()
# <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

# Retrieve the book
book1 = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book1.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>

