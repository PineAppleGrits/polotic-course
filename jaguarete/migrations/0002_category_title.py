# Generated by Django 3.2.4 on 2021-07-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaguarete', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='Categoria', max_length=30),
        ),
    ]