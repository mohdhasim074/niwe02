# Generated by Django 4.2.15 on 2024-09-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document_Section', '0023_delete_annualreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='annual-reports/')),
                ('docs', models.FileField(upload_to='annual-reports/')),
            ],
        ),
    ]
