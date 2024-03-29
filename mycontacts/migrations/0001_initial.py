# Generated by Django 4.2.2 on 2023-06-16 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mycontacts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lisiting", models.CharField(max_length=200)),
                ("listing_id", models.CharField(max_length=200)),
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=100)),
                ("message", models.TextField(blank=True)),
                (
                    "contact_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("user_id", models.IntegerField(blank=True)),
            ],
        ),
    ]
