# Generated by Django 4.2.15 on 2024-09-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0064_sdt_eitc_trainings_sdt_eitc_sub_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDT_Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_type', models.CharField(max_length=250)),
                ('serial', models.IntegerField()),
                ('title_of_magzines', models.CharField(max_length=200)),
                ('subcription_status', models.CharField(max_length=50)),
            ],
        ),
    ]
