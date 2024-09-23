# Generated by Django 5.0.6 on 2024-06-21 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff_Section', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificationAndInformationTechnologyStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, default='Not Avaliable', max_length=20)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CertiAndInfoTechStaff',
        ),
        migrations.AlterField(
            model_name='financeandadministrationstaff',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offshorewinddevelopstaff',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='researchanddevelopmentstaff',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skilldevelopmentandtrainingstaff',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='testingstandardsandregulationstaff',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='windresourceassessmentstaff',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]