# Generated by Django 3.1.4 on 2021-04-05 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0031_remove_hotelroom_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='city',
        ),
    ]
