from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # الحقول الموجودة فقط
    list_filter = ('author', 'publication_year')             # الفلاتر على الحقول الموجودة فقط
    search_fields = ('title', 'author')                       # الحقول التي سيتم البحث فيها
