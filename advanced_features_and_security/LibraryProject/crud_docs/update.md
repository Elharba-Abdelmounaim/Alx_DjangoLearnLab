# Update a Book

```python
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

```

- Output:
- Nineteen Eighty-Four


---

### 🗑️ **Delete**
```python
book.delete()
print(Book.objects.all())