from django.contrib import admin
from .models import Author,Book,Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','photo')

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)


