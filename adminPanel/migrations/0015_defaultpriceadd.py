# Generated by Django 3.1.4 on 2021-04-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0014_auto_20210407_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultPriceAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_price', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
        ),
    ]
