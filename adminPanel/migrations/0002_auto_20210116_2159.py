# Generated by Django 3.1.4 on 2021-01-16 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminPanel', '0001_initial'),
        ('themedTour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='themedpackreservation',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='themedTour.orderedthemedpack'),
        ),
        migrations.AddField(
            model_name='themedpackreservation',
            name='pack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themedTour.themedpack'),
        ),
    ]
