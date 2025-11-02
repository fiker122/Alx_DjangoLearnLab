
---

### **3️⃣ update.md**

```markdown
# Update the Book title

```python
from bookshelf.models import Book

# Retrieve the book
book1 = Book.objects.get(title="1984")

# Update title
book1.title = "Nineteen Eighty-Four"
book1.save()

# Confirm update
Book.objects.all()
# <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
