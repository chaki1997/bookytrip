# Generated by Django 3.1.4 on 2021-03-27 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0026_roompicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roompicture',
            name='picture',
            field=models.ImageField(upload_to='images/accomodation'),
        ),
    ]