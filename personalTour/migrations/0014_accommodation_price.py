# Generated by Django 3.1.4 on 2021-02-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0013_accomodationcheckout'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
