
---

### **4️⃣ delete.md**

```markdown
# Delete the Book instance

```python
from bookshelf.models import Book

# Retrieve the book
book1 = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book1.delete()

# Confirm deletion
Book.objects.all()
# <QuerySet []>
