# Generated by Django 5.0.6 on 2024-06-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Media_Section', '0006_citizen_charter_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='url',
            field=models.URLField(blank=True, default='Empty', null=True),
        ),
    ]
