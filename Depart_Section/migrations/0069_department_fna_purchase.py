# Generated by Django 4.2.15 on 2024-09-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0068_remove_sdt_globalwindday_url_sdt_global_sub_wind'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department_Fna_Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annexure', models.CharField(max_length=200)),
                ('docs', models.FileField(upload_to='departs/')),
            ],
        ),
    ]
