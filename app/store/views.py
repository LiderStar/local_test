from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author
from .serializers import BooksSerializers


# Create your views here.
def index(requests):
    return HttpResponse("Its OK")


def view(request):
    return HttpResponse(Book.objects.all())


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializers
    queryset = Book.objects.all()
    serializer = BooksSerializers(queryset)


class BookListView(ListView):
    model = Book
    paginate_by = 50
    template_name = "store/book_list.html"
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.all()


class AuthorListView(ListView):
    model = Book
    paginate_by = 50
    template_name = "store/author_list.html"
    context_object_name = 'author_list'

    def get_queryset(self):
        author = get_object_or_404(Author, name=self.kwargs.get('author'))
        return Book.objects.filter(author=author.id).order_by('title')

        #
        # def get_queryset(self):
        #     user = get_object_or_404(User, username=self.kwargs.get('username'))
        #     return Post.objects.filter(author=user.id).order_by('-title')