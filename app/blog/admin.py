from django.contrib import admin
from .models import Post


# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'date_create', 'date_update', 'author', 'is_published']
    list_display_links = ['title']
    search_fields = ['title', 'content', 'author']
    list_editable = ('is_published',)
    list_filter = ('title', 'content', 'author',)