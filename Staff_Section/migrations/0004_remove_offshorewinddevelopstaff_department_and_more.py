# Generated by Django 5.0.6 on 2024-06-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff_Section', '0003_alter_certificationandinformationtechnologystaff_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offshorewinddevelopstaff',
            name='department',
        ),
        migrations.RemoveField(
            model_name='researchanddevelopmentstaff',
            name='department',
        ),
        migrations.RemoveField(
            model_name='skilldevelopmentandtrainingstaff',
            name='department',
        ),
        migrations.RemoveField(
            model_name='windresourceassessmentstaff',
            name='department',
        ),
        migrations.AlterField(
            model_name='certificationandinformationtechnologystaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='financeandadministrationstaff',
            name='email',
            field=models.CharField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='financeandadministrationstaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='offshorewinddevelopstaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='researchanddevelopmentstaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='skilldevelopmentandtrainingstaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='testingstandardsandregulationstaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='windresourceassessmentstaff',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
