from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.
# --- CRUD Views for Book ---

# List all books / Create new book
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: list = anyone, create = only authenticated
    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


# Retrieve / Update / Delete single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: update/delete = only authenticated
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
