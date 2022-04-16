from django.contrib import admin

from books.models import Book, Entry, Review, Topic

# Register your models here.

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Topic)
admin.site.register(Entry)