# Generated by Django 3.1.1 on 2021-04-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0003_auto_20210401_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(verbose_name=('%I:%M %p',)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(verbose_name=('%I:%M %p',)),
        ),
    ]