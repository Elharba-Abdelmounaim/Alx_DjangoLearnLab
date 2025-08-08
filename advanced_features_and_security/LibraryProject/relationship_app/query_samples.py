import os
import django
import sys

# 👇 إضافة مجلد المشروع إلى sys.path ليتمكن Python من إيجاد إعدادات Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 👇 إعداد البيئة باستخدام المسار الكامل للملف settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter 1", author=author)
    book2 = Book.objects.create(title="Harry Potter 2", author=author)

    library = Library.objects.create(name="Central Library")
    library.books.add(book1, book2)

    librarian = Librarian.objects.create(name="John Doe", library=library)

def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(f"Book: {book.title}")

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    for book in library.books.all():
        print(f"Book in {library.name}: {book.title}")

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    print(f"Librarian of {library.name}: {library.librarian.name}")

if __name__ == "__main__":
    create_sample_data()
    query_books_by_author("J.K. Rowling")
    query_books_in_library("Central Library")
    query_librarian_for_library("Central Library")
