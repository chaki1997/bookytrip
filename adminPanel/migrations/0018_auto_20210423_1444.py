# Generated by Django 3.1.4 on 2021-04-23 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0017_whyus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whyus',
            old_name='titile',
            new_name='title',
        ),
    ]