# Generated by Django 3.1.4 on 2021-04-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='access_adminpanel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='access_components',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='access_perosnaltour',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='access_themedtour',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='access_users',
            field=models.BooleanField(default=False),
        ),
    ]
