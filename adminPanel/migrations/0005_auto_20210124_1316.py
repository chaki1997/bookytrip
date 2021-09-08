# Generated by Django 3.1.4 on 2021-01-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0004_themedpackreservation_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='themedpackreservation',
            name='price',
        ),
        migrations.AddField(
            model_name='themedpackreservation',
            name='calendar_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
