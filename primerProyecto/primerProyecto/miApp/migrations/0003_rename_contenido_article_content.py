# Generated by Django 5.0.2 on 2024-02-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_article_image_alter_article_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='contenido',
            new_name='content',
        ),
    ]
