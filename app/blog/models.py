from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = 'Создать пост'
        verbose_name_plural = "Создать посты"
        ordering = ['date_create']

    title = models.CharField(max_length=256, db_index=True, help_text="Не больше 256 символов", verbose_name="Название")
    # content = models.TextField(blank=True, null=True)
    content = CKEditor5Field(max_length=5000, blank=True, null=True, help_text="Не больше 5000 символов", verbose_name="Контент")
    date_create = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор")
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True)
    likes = models.ManyToManyField(User, related_name='likes_post', blank=True, verbose_name="Лайки")
    reply = models.ForeignKey('self', null=True, related_name='reply_post', on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse_lazy('view_post', kwargs={'slug': self.slug})
        # return f'/posts/{self.slug}/'

    def __str__(self):
        return self.title


class Profile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    about = models.TextField(max_length=5000, verbose_name='О себе', help_text='Не больше 5000 символов')
    profile_img = models.ImageField(upload_to='profile_images/%Y/%m/%D/', default='blank-profile-picture.png', verbose_name="Аватар")
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Создать профиль'
        verbose_name_plural = "Создать профили"
        ordering = ['-author']


