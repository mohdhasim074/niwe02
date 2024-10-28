# Generated by Django 4.2.15 on 2024-09-18 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0015_department_testing_measuretype'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDT_workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SDT_workshop_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depart_Section.sdt_workshop')),
            ],
        ),
    ]