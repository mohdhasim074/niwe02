# Generated by Django 5.0.6 on 2024-06-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_section', '0006_alter_director_general_office_staff_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director_general_office_staff',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='director_general_office_staff',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
