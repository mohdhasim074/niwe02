# Generated by Django 4.2.15 on 2024-09-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document_Section', '0021_newsletters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletters',
            name='docs',
            field=models.FileField(upload_to='pdf/'),
        ),
    ]