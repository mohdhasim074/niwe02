# Generated by Django 5.0.6 on 2024-06-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_section', '0005_director_general_message_dirs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director_general_office_staff',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]
