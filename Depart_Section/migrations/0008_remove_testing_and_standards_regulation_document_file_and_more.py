# Generated by Django 5.0.6 on 2024-08-21 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0007_alter_skill_developements_training_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testing_and_standards_regulation',
            name='document_File',
        ),
        migrations.AlterField(
            model_name='testing_and_standards_regulation',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
