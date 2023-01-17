from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'date_create', 'date_update', 'author', ]
