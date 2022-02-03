# Generated by Django 3.2.10 on 2022-02-03 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="users.customuser",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="organizations.organization",
                    ),
                ),
            ],
        ),
    ]
