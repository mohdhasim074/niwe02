# Generated by Django 4.2.15 on 2024-10-24 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0081_delete_relatedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sdt_short_term',
            name='image',
        ),
    ]