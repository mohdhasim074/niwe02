# Generated by Django 4.2.15 on 2024-09-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0022_rename_internationaltraining_sdt_internationaltraining'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sdt_internationaltraining',
            old_name='year',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='sdt_internationaltraining',
            name='docs',
            field=models.URLField(),
        ),
    ]
