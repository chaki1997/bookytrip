# Generated by Django 3.1.1 on 2021-09-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0049_hotelorder_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='type',
            field=models.CharField(default='hotel', max_length=10),
        ),
    ]
