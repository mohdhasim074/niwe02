# Generated by Django 4.2.15 on 2024-09-18 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0014_delete_department_testing_measuretype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department_testing_measureType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('year', models.CharField(max_length=100)),
                ('project_number', models.CharField(max_length=100)),
                ('testing_type_with_company_name', models.CharField(max_length=100)),
                ('agreement_signed', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depart_Section.department_testing_measure')),
            ],
        ),
    ]
