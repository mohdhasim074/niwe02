# Generated by Django 4.2.15 on 2024-09-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0040_rename_url_sdt_customize_training_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdt_internationaltraining',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='sdt_national',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
