# Generated by Django 4.2.15 on 2024-09-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0024_rename_docs_sdt_internationaltraining_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customize_Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
    ]
