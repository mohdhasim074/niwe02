# Generated by Django 4.2.15 on 2024-09-25 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0060_rename_wra_srra_station_phase_wra_srra_station_phases_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WRA_Srra_Station_ams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('comission_date', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('elavation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WRA_Srra_Station_anert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('comission_date', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('elavation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WRA_Srra_Station_meda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('comission_date', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('elavation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WRA_Srra_Station_phaseII',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.IntegerField()),
                ('station_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('comission_date', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=3, max_digits=10)),
                ('elavation', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='wra_srra_station_phases',
            name='head',
        ),
        migrations.RemoveField(
            model_name='wra_srra_station_phases',
            name='phase_type',
        ),
    ]