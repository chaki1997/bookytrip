# Generated by Django 3.1.4 on 2021-02-25 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0010_city'),
        ('personalTour', '0018_auto_20210224_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminPanel.city'),
        ),
    ]
