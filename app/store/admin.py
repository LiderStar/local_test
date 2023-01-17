from django.contrib import admin
from .models import Book, Author, Client


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'amount', 'price', ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'phone', 'email', 'discount', ]
