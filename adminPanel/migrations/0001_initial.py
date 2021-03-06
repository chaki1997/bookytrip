# Generated by Django 3.1.4 on 2021-01-16 21:59

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Country',
            },
        ),
        migrations.CreateModel(
            name='FooterDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phoneKA', models.CharField(default='+995 ', max_length=100)),
                ('phoneEN', models.CharField(default='+44 ', max_length=100)),
                ('phoneFR', models.CharField(default='+33 ', max_length=100)),
                ('phoneAZ', models.CharField(default='+994 ', max_length=100)),
                ('phoneDE', models.CharField(default='+49 ', max_length=100)),
                ('phoneES', models.CharField(default='+34 ', max_length=100)),
                ('phoneHY', models.CharField(default='+374 ', max_length=100)),
                ('phoneIT', models.CharField(default='+39 ', max_length=100)),
                ('phoneRU', models.CharField(default='+7 ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ThemedPackDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='ThemedPackReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ThemedPackVariety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_variety', models.CharField(max_length=256)),
            ],
        ),
    ]
