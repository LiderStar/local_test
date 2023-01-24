from django.db import models
from django.urls import reverse, reverse_lazy
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    title = models.CharField('Title', max_length=200)
    text = CKEditor5Field('Text', config_name='extends')


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name="AUTHOR")

    def __str__(self):
        return self.name


class Client(models.Model):
    firstname = models.CharField(max_length=256, verbose_name="FIRST_NAME")
    lastname = models.CharField(max_length=256, verbose_name="LAST_NAME")
    phone = models.CharField(max_length=28, verbose_name="PHONE")
    email = models.EmailField()
    discount = models.DecimalField(max_digits=2, decimal_places=1, verbose_name="DISCOUNT")

    def __str__(self):
        return self.firstname

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=256, verbose_name="TITLE")
    amount = models.IntegerField(verbose_name="AMOUNT")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="PRICE")
    anotation = models.TextField(max_length=2000, blank=True)
    client = models.ManyToManyField(Client)

    def get_absolute_url(self):
        return reverse('store:author_list', kwargs={'author': self.author})

    def __str__(self):
        return self.title

