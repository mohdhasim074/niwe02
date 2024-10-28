# Generated by Django 4.2.15 on 2024-09-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0053_remove_sdt_customize_training_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdt_internationaltraining',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='sdt_internationaltraining_eitec',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='sdt_internationaltraining_sub_eitec',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]