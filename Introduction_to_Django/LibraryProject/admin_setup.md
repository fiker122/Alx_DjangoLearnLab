# D# Django Admin Setup for Book Model

1. Registered the Book model in `bookshelf/admin.py`.
2. Customized the admin view:
   - `list_display = ('title', 'author', 'publication_year')`
   - `search_fields = ('title', 'author')`
   - `list_filter = ('publication_year',)`
3. Created a superuser using `python manage.py createsuperuser`.
4. Accessed the admin interface at http://127.0.0.1:8000/admin/ and verified CRUD operations.
