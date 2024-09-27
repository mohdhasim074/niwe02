# Generated by Django 5.0.6 on 2024-09-27 11:29

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depart_Section', '0075_alter_sdt_vayumitra_title_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sdt_vayumitra',
            name='title_type',
        ),
        migrations.RemoveField(
            model_name='sdt_vayumitra',
            name='url',
        ),
        migrations.AlterField(
            model_name='finance_and_administration',
            name='NIWE_Pan_ARN_GST_Details',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='finance_and_administration',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='sdt_eitc_sub_training',
            name='data',
            field=tinymce.models.HTMLField(blank=True, default='.'),
        ),
        migrations.AlterField(
            model_name='sdt_training_sub_calender',
            name='data',
            field=tinymce.models.HTMLField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wind_resources_assessment',
            name='description',
            field=tinymce.models.HTMLField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wra_sale_publication',
            name='total_amount2',
            field=models.CharField(blank=True, default=1),
            preserve_default=False,
        ),
    ]