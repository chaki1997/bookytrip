# Generated by Django 3.1.4 on 2021-04-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0018_auto_20210423_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_text', models.TextField()),
                ('title1', models.CharField(max_length=127)),
                ('image1', models.ImageField(upload_to='')),
                ('title2', models.CharField(max_length=127)),
                ('image2', models.ImageField(upload_to='')),
                ('title3', models.CharField(max_length=127)),
                ('image3', models.ImageField(upload_to='')),
            ],
        ),
    ]
