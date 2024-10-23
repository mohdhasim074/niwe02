# Generated by Django 5.0.6 on 2024-06-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_section', '0007_alter_director_general_office_staff_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director_general_office_staff',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='director_general_office_staff',
            name='email',
            field=models.CharField(blank=True, default='Not Avaliable', max_length=20),
        ),
    ]
