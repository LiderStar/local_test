from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Book
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