from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    #  Filters, Searching, Ordering
    filter_backends = [
        django_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    #  Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    #  Searching
    search_fields = ['title', 'author']

    #  Ordering
    ordering_fields = ['title', 'author', 'publication_year']
    ordering = ['title']  # default ordering
