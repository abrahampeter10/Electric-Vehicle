# Generated by Django 5.0 on 2023-12-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargingstations', '0004_alter_add_charg_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_charg',
            name='image',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]
