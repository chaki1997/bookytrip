# Generated by Django 3.1.4 on 2021-05-03 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0020_auto_20210423_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='title1',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='about',
            name='title3',
        ),
    ]