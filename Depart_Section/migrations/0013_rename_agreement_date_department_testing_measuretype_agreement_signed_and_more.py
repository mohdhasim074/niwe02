# Generated by Django 4.2.15 on 2024-09-18 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0012_department_testing_measuretype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department_testing_measuretype',
            old_name='agreement_date',
            new_name='agreement_signed',
        ),
        migrations.RenameField(
            model_name='department_testing_measuretype',
            old_name='company_name',
            new_name='testing_type_with_company_name',
        ),
    ]