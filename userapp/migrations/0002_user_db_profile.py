# Generated by Django 5.0 on 2024-01-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_db',
            name='profile',
            field=models.ImageField(default=True, upload_to='profile'),
        ),
    ]
