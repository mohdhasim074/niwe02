# Generated by Django 4.2.15 on 2024-09-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0041_alter_sdt_internationaltraining_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdt_national',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='sdt_national',
            name='url',
            field=models.URLField(),
        ),
    ]
