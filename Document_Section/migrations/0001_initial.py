# Generated by Django 5.0.6 on 2024-06-20 10:38

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year_of_Report', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='DiffBetweenFosilFuelWind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField()),
                ('fosil_Fuel', tinymce.models.HTMLField()),
                ('Wind_Energy', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FAQs', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='RecordsRetentionSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ministry_Approval', models.FileField(upload_to='pdf/')),
                ('NIEW_Records_Retention_Schedule', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='RevisedGuidelinesForProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_No', models.IntegerField()),
                ('description', tinymce.models.HTMLField()),
                ('date', models.DateField()),
            ],
        ),
    ]
