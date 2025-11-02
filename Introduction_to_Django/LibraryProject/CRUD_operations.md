1.Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984>
2.Retrieve
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
# Output: 1984 George Orwell 1949
3.Update
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)
# Output: Nineteen Eighty-Four
4.Delete
retrieved_book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
