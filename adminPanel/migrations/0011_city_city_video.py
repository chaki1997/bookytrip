# Generated by Django 3.1.4 on 2021-03-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0010_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='city_video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
