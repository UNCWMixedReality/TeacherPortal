# Generated by Django 3.2.10 on 2022-03-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_alter_headset_device_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headset',
            name='device_id',
            field=models.CharField(default='UNREGISTERED_HEADSET', max_length=128, unique=True),
        ),
    ]
