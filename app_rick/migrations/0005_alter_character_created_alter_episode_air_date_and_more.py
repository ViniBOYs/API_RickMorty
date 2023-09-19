# Generated by Django 4.2.4 on 2023-08-29 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rick', '0004_alter_character_created_alter_episode_air_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 11, 7, 951781, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 11, 7, 951781, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='location',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 11, 7, 951781, tzinfo=datetime.timezone.utc)),
        ),
    ]
