# Generated by Django 3.1.4 on 2021-02-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0017_ordercar'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationreview',
            name='stars',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='carreview',
            name='stars',
            field=models.SmallIntegerField(default=5),
        ),
    ]
