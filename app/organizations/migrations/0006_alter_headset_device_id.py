# Generated by Django 3.2.10 on 2022-03-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_remove_headset_device_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headset',
            name='device_id',
            field=models.CharField(default='UNREGISTERED_HEADSET', max_length=128),
        ),
    ]
