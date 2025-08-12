from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

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
