# Generated by Django 4.2.2 on 2023-06-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("technology", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="gallery")),
                ("link", models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Work",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("description2", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="gallery")),
                ("link", models.URLField(null=True)),
            ],
        ),
    ]
