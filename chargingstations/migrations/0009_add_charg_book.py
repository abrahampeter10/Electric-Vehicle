# Generated by Django 5.0 on 2024-02-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargingstations', '0008_remove_add_charg_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_charg',
            name='book',
            field=models.BooleanField(default=False),
        ),
    ]