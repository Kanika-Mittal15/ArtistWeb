# Generated by Django 3.1.3 on 2020-11-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20201117_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=''),
        ),
    ]
