# Generated by Django 5.0.4 on 2024-04-17 01:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
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
                ("name", models.CharField(max_length=40)),
                ("document", models.CharField(max_length=15, unique=True)),
                ("phone", models.CharField(max_length=15)),
                ("date_birth", models.DateField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now_add=True)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "profile",
                    models.CharField(
                        choices=[
                            ("A", "Apostador"),
                            ("B", "Blogueiro"),
                            ("N", "Normal"),
                        ],
                        default="N",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deposit",
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
                    "value",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                ("balance_after", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="bear.player"
                    ),
                ),
            ],
        ),
    ]