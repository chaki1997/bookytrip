# Generated by Django 3.1.4 on 2021-06-23 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0038_accommodation_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='price',
        ),
    ]
