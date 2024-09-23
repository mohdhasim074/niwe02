# Generated by Django 5.0.6 on 2024-06-19 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='WRA',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Depart_Section.wind_resources_assessment'),
        ),
    ]
