# Generated by Django 3.1.4 on 2021-05-03 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0032_remove_apartment_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='notification',
            field=models.BooleanField(default=False),
        ),
    ]