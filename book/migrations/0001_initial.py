# Generated by Django 5.1.1 on 2024-09-27 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100, verbose_name="论坛名")),
                ("description", models.TextField(verbose_name="论坛简介")),
                (
                    "image",
                    models.ImageField(
                        upload_to="book/images/", verbose_name="论坛封面"
                    ),
                ),
                ("url", models.URLField(blank=True, verbose_name="论坛链接")),
            ],
            options={
                "verbose_name": "论坛",
                "verbose_name_plural": "论坛",
            },
        ),
    ]
