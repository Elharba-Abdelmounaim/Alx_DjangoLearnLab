# relationship_app/views.py

from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

#  دالة عرض بسيطة تعيد الكتب كنص عادي
def list_books(request):
    books = Book.objects.all()
    text_list = "\n".join(f"{book.title} by {book.author.name}" for book in books)
    return HttpResponse(text_list, content_type="text/plain")

# عرض صفّي باستخدام DetailView لمكتبة معينة
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
