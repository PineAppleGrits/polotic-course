# Generated by Django 3.2.4 on 2021-07-02 14:05

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete', '0003_auto_20210702_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=pathlib.PurePosixPath('/mnt/c/Users/Gino/Desktop/polotic/polotic/media')),
        ),
    ]
