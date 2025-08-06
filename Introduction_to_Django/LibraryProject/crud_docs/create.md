# Create Book

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

---

### 📄 `crud_docs/retrieve.md`

```md
# Retrieve Book

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

---