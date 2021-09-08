# Generated by Django 3.1.4 on 2021-03-27 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0025_auto_20210327_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='images/brand-2.jpg', upload_to='images/accomodation')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalTour.hotelroom')),
            ],
        ),
    ]