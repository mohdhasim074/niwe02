# Generated by Django 4.2.15 on 2024-09-18 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0016_sdt_workshop_sdt_workshop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdt_workshop',
            name='url',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
