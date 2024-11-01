# Generated by Django 5.0 on 2024-02-07 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketPlaces', '0003_rename_cid_c_category_vid'),
        ('userapp', '0005_remove_chargingslotbooking_vid'),
    ]

    operations = [
        migrations.CreateModel(
            name='mar_vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehName', models.CharField(max_length=50)),
                ('VehType', models.CharField(max_length=50)),
                ('VehModel', models.CharField(max_length=50)),
                ('VehDrive', models.CharField(max_length=50)),
                ('VehSeat', models.CharField(max_length=50)),
                ('VehBattery', models.CharField(max_length=50)),
                ('VehRate', models.CharField(max_length=50)),
                ('VehImg', models.ImageField(default=True, upload_to='image')),
                ('Date', models.CharField(max_length=14)),
                ('status', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('reject', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.user_db')),
                ('vid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarketPlaces.comp_db')),
            ],
        ),
    ]
