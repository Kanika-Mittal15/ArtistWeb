# Generated by Django 3.1.3 on 2021-01-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0041_auto_20210121_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', max_length=255, null=True, upload_to='profile_pics'),
        ),
    ]
