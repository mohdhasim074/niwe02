# Generated by Django 4.2.15 on 2024-09-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0008_remove_testing_and_standards_regulation_document_file_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wind_Terbine_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terbine_photo', models.ImageField(upload_to='subalbums/')),
            ],
        ),
    ]