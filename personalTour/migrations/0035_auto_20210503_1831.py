# Generated by Django 3.1.4 on 2021-05-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0034_auto_20210503_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='notification',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='notification',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='notification',
            field=models.BooleanField(default=False),
        ),
    ]
