# Generated by Django 5.0.6 on 2024-06-18 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Section', '0003_rename_media_award'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='image_1',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='award',
            name='image_2',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]