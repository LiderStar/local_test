from django.db import models
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


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=256, verbose_name="TITLE")
    amount = models.IntegerField(verbose_name="AMOUNT")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="PRICE")
    client = models.ManyToManyField(Client, null=True)

    def __str__(self):
        return self.title
