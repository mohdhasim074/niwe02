# Generated by Django 4.2.15 on 2024-09-19 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0020_alter_sdt_vayumitra_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdt_vayumitra',
            name='serial',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
