# bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm
from .models import Book
from django.db.models import Q

def search_books(request):
    form = ExampleForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
