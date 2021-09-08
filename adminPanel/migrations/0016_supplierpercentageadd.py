# Generated by Django 3.1.4 on 2021-04-23 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminPanel', '0015_defaultpriceadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierPercentageAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]