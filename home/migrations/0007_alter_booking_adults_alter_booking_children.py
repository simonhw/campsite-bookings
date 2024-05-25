# Generated by Django 4.2.13 on 2024-05-24 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_booking_options_alter_booking_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='adults',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='children',
            field=models.PositiveIntegerField(default=0),
        ),
    ]