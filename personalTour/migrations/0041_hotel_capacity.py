# Generated by Django 3.1.4 on 2021-06-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0040_hotelorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
