# Generated by Django 3.1.4 on 2021-02-04 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0008_auto_20210124_1530'),
        ('personalTour', '0004_auto_20210204_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='destination',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminPanel.country'),
        ),
    ]
