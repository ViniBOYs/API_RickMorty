# Generated by Django 4.2.4 on 2023-08-22 23:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_rick', '0003_location_rename_species_specie_delete_locations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 47, 37, 230704, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 47, 37, 230704, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='location',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 47, 37, 230704, tzinfo=datetime.timezone.utc)),
        ),
    ]
