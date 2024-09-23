# Generated by Django 5.0.6 on 2024-06-21 06:36

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document_Section', '0004_rename_preambel_faqs_preamble'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('linkTitle', tinymce.models.HTMLField()),
            ],
        ),
    ]