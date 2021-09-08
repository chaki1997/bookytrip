# Generated by Django 3.1.4 on 2021-06-18 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0023_auto_20210503_1503'),
        ('personalTour', '0037_auto_20210520_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodation',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminPanel.city'),
        ),
    ]