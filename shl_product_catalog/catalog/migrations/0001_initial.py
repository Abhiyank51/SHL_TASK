# Generated by Django 5.1.7 on 2025-04-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assessment",
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
                ("name", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=50)),
                ("role", models.CharField(max_length=50)),
                ("industry", models.CharField(max_length=50)),
                ("skills", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
    ]
