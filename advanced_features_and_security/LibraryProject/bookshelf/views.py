from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import render
from django.db.models import Q
from .forms import SearchForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
   
    pass

def search_books(request):
    form = SearchForm(request.GET or None)
    books = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']
       
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request, 'bookshelf/search_results.html', {'form': form, 'books': books})