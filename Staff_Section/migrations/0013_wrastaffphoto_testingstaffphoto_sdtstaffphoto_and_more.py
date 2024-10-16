# Generated by Django 4.2.15 on 2024-09-13 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff_Section', '0012_owdstaffphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='WRAStaffPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='subalbums/')),
                ('Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('Specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('Areas_Of_Interest', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_Joining', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff_Section.windresourceassessmentstaff')),
            ],
        ),
        migrations.CreateModel(
            name='TestingStaffPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='subalbums/')),
                ('Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('Specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('Areas_Of_Interest', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_Joining', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff_Section.testingstandardsandregulationstaff')),
            ],
        ),
        migrations.CreateModel(
            name='SDTStaffPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='subalbums/')),
                ('Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('Specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('Areas_Of_Interest', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_Joining', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff_Section.skilldevelopmentandtrainingstaff')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchStaffPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='subalbums/')),
                ('Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('Specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('Areas_Of_Interest', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_Joining', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff_Section.researchanddevelopmentstaff')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceStaffPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='subalbums/')),
                ('Designation', models.CharField(blank=True, max_length=100, null=True)),
                ('Qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('Specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('Areas_Of_Interest', models.CharField(blank=True, max_length=200, null=True)),
                ('Year_of_Joining', models.CharField(blank=True, max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff_Section.financeandadministrationstaff')),
            ],
        ),
    ]
