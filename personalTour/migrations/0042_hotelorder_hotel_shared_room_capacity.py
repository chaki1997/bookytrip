# Generated by Django 3.1.4 on 2021-06-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0041_hotel_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelorder',
            name='hotel_shared_room_capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
