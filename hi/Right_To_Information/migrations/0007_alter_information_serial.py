# Generated by Django 4.2.15 on 2024-10-22 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Right_To_Information', '0006_information_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='serial',
            field=models.IntegerField(default=1),
        ),
    ]
