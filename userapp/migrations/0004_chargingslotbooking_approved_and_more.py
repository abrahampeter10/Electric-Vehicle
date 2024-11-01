# Generated by Django 5.0 on 2024-02-01 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaces', '0003_rename_cid_c_category_vid'),
        ('userapp', '0003_chargingslotbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingslotbooking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chargingslotbooking',
            name='reject',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chargingslotbooking',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chargingslotbooking',
            name='vid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MarketPlaces.comp_db'),
            preserve_default=False,
        ),
    ]