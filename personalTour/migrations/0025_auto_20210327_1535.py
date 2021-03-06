# Generated by Django 3.1.4 on 2021-03-27 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personalTour', '0024_hotelcheckout_hotelorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomCheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalTour.hotelroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_order_start_date', models.DateField()),
                ('room_order_end_date', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalTour.hotelroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='hotelorder',
            name='accommodation',
        ),
        migrations.RemoveField(
            model_name='hotelorder',
            name='room',
        ),
        migrations.RemoveField(
            model_name='hotelorder',
            name='user',
        ),
        migrations.DeleteModel(
            name='HotelCheckout',
        ),
        migrations.DeleteModel(
            name='HotelOrder',
        ),
    ]
