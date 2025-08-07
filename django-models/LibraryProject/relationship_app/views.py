# relationship_app/views.py

from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

#  دالة عرض بسيطة تعيد الكتب كنص عادي
def list_books(request):
     books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# عرض صفّي باستخدام DetailView لمكتبة معينة
class LibraryDetailView(DetailView):
     model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
