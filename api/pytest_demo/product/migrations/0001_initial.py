# Generated by Django 4.1.7 on 2023-03-31 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=15, unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("In Stock", "In Stock"),
                            ("Out of Stock", "Out Of Stock"),
                        ],
                        default="In Stock",
                        max_length=30,
                    ),
                ),
                (
                    "last_updated",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]