# Generated by Django 4.2.15 on 2024-09-09 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Section', '0010_album_subgallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='description',
        ),
        migrations.RemoveField(
            model_name='subgallery',
            name='description',
        ),
    ]