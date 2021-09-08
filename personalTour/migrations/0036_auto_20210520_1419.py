# Generated by Django 3.1.4 on 2021-05-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalTour', '0035_auto_20210503_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomcheckout',
            name='room_checkout',
        ),
        migrations.RemoveField(
            model_name='roomcheckout',
            name='user',
        ),
        migrations.RemoveField(
            model_name='roomorder',
            name='room',
        ),
        migrations.RemoveField(
            model_name='roomorder',
            name='user',
        ),
        migrations.RemoveField(
            model_name='roompicture',
            name='room',
        ),
        migrations.AddField(
            model_name='hotel',
            name='bed_type',
            field=models.CharField(blank=True, choices=[('1', 'Twin'), ('2', 'Double'), ('3', 'Triple'), ('4', 'Shared')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='family',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotel',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='images/accomodation'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='picture2',
            field=models.ImageField(blank=True, null=True, upload_to='images/accomodation'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='picture3',
            field=models.ImageField(blank=True, null=True, upload_to='images/accomodation'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='picture4',
            field=models.ImageField(blank=True, null=True, upload_to='images/accomodation'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='images/accomodation'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
        migrations.AddField(
            model_name='hotel',
            name='room_type',
            field=models.CharField(blank=True, choices=[('1', 'Independent room'), ('2', 'Shared room'), ('3', 'Private room')], max_length=256, null=True),
        ),
        migrations.DeleteModel(
            name='HotelRoom',
        ),
        migrations.DeleteModel(
            name='RoomCheckout',
        ),
        migrations.DeleteModel(
            name='RoomOrder',
        ),
        migrations.DeleteModel(
            name='RoomPicture',
        ),
    ]