from django.contrib import admin
from .models import Book

# Customize the admin interface for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show in list
    search_fields = ('title', 'author')                     # searchable fields
    list_filter = ('publication_year',)                    # filter by publication year

# Register the Book model with custom admin
admin.site.register(Book, BookAdmin)
