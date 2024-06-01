from django.contrib import admin
from book.models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date','description','price', 'cover_image', 'category')

admin.site.register(Book, BookAdmin)