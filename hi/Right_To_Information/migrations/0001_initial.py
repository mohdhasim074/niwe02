# Generated by Django 5.0.6 on 2024-06-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RightToInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=20)),
                ('document', models.FileField(blank=True, null=True, upload_to='pdf/')),
            ],
        ),
    ]