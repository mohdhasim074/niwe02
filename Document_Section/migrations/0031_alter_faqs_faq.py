# Generated by Django 4.2.15 on 2024-10-11 15:25

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Document_Section', '0030_alter_generalinformation_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='Faq',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]