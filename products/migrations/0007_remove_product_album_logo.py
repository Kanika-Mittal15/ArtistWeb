# Generated by Django 3.1.3 on 2020-11-13 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_hotel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='album_logo',
        ),
    ]
