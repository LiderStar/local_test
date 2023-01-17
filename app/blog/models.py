from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    class Meta:
        verbose_name = 'Create post'
        verbose_name_plural = "Create post's"
    title = models.CharField(max_length=256)
    content = models.TextField(blank=True, null=True)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

