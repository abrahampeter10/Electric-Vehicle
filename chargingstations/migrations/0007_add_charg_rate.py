# Generated by Django 5.0 on 2024-01-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargingstations', '0006_charging_reg_image_charging_reg_phnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_charg',
            name='rate',
            field=models.CharField(default=True, max_length=10),
        ),
    ]
