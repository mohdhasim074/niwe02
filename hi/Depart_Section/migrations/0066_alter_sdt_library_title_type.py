# Generated by Django 4.2.15 on 2024-09-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0065_sdt_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdt_library',
            name='title_type',
            field=models.CharField(default='Library Type', max_length=50),
        ),
    ]