# Generated by Django 4.2.13 on 2024-05-24 13:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_booking_adults_alter_booking_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
    ]
