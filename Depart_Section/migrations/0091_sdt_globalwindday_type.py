# Generated by Django 4.2.15 on 2024-10-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0090_sdt_globalwindday_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdt_globalwindday',
            name='type',
            field=models.CharField(default='url', max_length=10),
        ),
    ]
