# Generated by Django 4.2.15 on 2024-10-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0086_rename_url_sdt_vayumitra_urls'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sdt_workshop',
            name='url',
        ),
        migrations.AddField(
            model_name='sdt_workshop_type',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]