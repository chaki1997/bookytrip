# Generated by Django 3.1.4 on 2021-05-13 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0010_auto_20210503_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='top_text',
        ),
        migrations.RemoveField(
            model_name='about',
            name='top_title',
        ),
    ]