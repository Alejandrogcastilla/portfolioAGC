# Generated by Django 4.1.1 on 2022-09-13 14:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mensajes",
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
                (
                    "fecha",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("nombre", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("mensaje", models.TextField(blank=True, max_length=4000)),
            ],
            options={
                "ordering": ["fecha"],
            },
        ),
        migrations.CreateModel(
            name="Visitas",
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
                (
                    "fecha",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                ("peticion", models.TextField()),
            ],
        ),
    ]
