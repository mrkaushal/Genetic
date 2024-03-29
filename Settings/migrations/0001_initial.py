# Generated by Django 3.1.1 on 2021-04-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hospital', models.CharField(max_length=60)),
                ('visible', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(null=True)),
                ('facebook', models.CharField(max_length=100)),
                ('link1', models.CharField(max_length=60)),
                ('link2', models.CharField(max_length=60)),
                ('link3', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'global_settings',
            },
        ),
    ]
