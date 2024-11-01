# Generated by Django 5.0 on 2023-12-08 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COMP_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('CmpName', models.CharField(max_length=30)),
                ('CmpId', models.CharField(max_length=30)),
                ('CmpLoc', models.CharField(max_length=70)),
                ('CmpState', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='C_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehName', models.CharField(max_length=100)),
                ('VehImg', models.ImageField(upload_to='VehImg')),
                ('VehType', models.CharField(max_length=25, null=True)),
                ('VehModel', models.CharField(max_length=50)),
                ('VehDrive', models.CharField(max_length=50)),
                ('VehSeat', models.CharField(max_length=50)),
                ('VehBattery', models.CharField(max_length=50)),
                ('VehRate', models.CharField(max_length=50)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MarketPlaces.comp_db')),
            ],
        ),
    ]