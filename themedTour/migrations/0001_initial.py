# Generated by Django 3.1.4 on 2021-01-16 21:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminPanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemedPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=50)),
                ('picture1', models.ImageField(default='images/brand-2.jpg', upload_to='images/themedpack')),
                ('picture2', models.ImageField(default='images/brand-2.jpg', upload_to='images/themedpack')),
                ('small_video', models.FileField(upload_to='themedvideos')),
                ('big_video', models.FileField(upload_to='themedvideos')),
                ('number_of_travelers', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('country', models.ManyToManyField(to='adminPanel.Country')),
                ('number_of_days', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminPanel.themedpackduration')),
                ('trip_variety', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adminPanel.themedpackvariety')),
            ],
            options={
                'verbose_name_plural': 'Themed Pack',
            },
        ),
        migrations.CreateModel(
            name='ThemedPackReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('stars', models.SmallIntegerField(default=5)),
                ('permition', models.BooleanField(default=False)),
                ('notification', models.BooleanField(default=False)),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themedTour.themedpack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Themed Pack Reviews',
            },
        ),
        migrations.CreateModel(
            name='ThemedDaysDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('pack_connect_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themedTour.themedpack')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedThemedPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_start_date', models.DateField()),
                ('order_end_date', models.DateField()),
                ('order_travelers', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='themedTour.themedpack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]