# Generated by Django 4.2.15 on 2024-10-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Right_To_Information', '0005_remove_information_url_subinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='serial',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
