# CRUD Operations for Book Model

## 1. Create

```python
from bookshelf.models import Book

# Create a Book instance
book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
book1
# Retrieve all Book objects
Book.objects.all()
# Update the title of the book
book.title = "Nineteen Eighty-Four"
book.save()

# Verify update
Book.objects.get(id=1).title
# Delete the book
book.delete()

# Verify deletion
Book.objects.all()


