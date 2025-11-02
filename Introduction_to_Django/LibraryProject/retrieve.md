
---

### **2️⃣ retrieve.md**

```markdown
# Retrieve the Book instance

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
# Create a Book instance 
