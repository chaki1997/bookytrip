# Generated by Django 3.1.4 on 2021-07-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0042_hotelorder_hotel_shared_room_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='bed_type',
            field=models.CharField(blank=True, choices=[('1', 'Twin'), ('2', 'Double'), ('3', 'Triple'), ('4', 'Suite'), ('5', 'Suite deluxe'), ('6', 'Triple'), ('7', 'Shared'), ('8', 'Custom')], max_length=256, null=True),
        ),
    ]