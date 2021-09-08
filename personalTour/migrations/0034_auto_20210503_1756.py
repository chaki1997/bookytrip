# Generated by Django 3.1.4 on 2021-05-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0033_auto_20210503_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='notification',
        ),
        migrations.AddField(
            model_name='apartment',
            name='notification',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotel',
            name='notification',
            field=models.BooleanField(default=False),
        ),
    ]
