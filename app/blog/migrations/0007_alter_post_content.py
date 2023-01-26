# Generated by Django 4.1.5 on 2023-01-18 07:43

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text="Не больше 5000 символов",
                max_length=5000,
                null=True,
            ),
        ),
    ]
