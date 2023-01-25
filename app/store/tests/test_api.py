from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BooksSerializers


class BookTestApi(APITestCase):
    def setUp(self) -> None:
        self.book_1 = Book.objects.create(author_id=3, title='Test book 1', price=25, amount=247)
        self.book_2 = Book.objects.create(author_id=3, title='Test book 2', price=225, amount=27)
        self.book_3 = Book.objects.create(author_id=3, title='Test book 3', price=215, amount=127)

    def test_get(self):

        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        print(response)
        serializer_data = BooksSerializers([self.book_1, self.book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test2_get(self):
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        print(response)
        serializer_data = BooksSerializers([book_1, book_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
