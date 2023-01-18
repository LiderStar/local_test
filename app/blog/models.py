from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = 'Create post'
        verbose_name_plural = "Create post's"

    title = models.CharField(max_length=256, db_index=True, help_text="Не больше 256 символов")
    # content = models.TextField(blank=True, null=True)
    content = CKEditor5Field(max_length=5000, blank=True, null=True, help_text="Не больше 5000 символов")
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.SlugField(max_length=50, unique=True)
    likes = models.ManyToManyField(User, related_name='likes_post', blank=True)
    reply = models.ForeignKey('self', null=True, related_name='reply_post', on_delete=models.CASCADE)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
