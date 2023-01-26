# Generated by Django 4.1.5 on 2023-01-18 06:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0003_alter_post_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]