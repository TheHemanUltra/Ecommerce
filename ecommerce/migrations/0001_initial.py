# Generated by Django 4.2.5 on 2023-10-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="products",
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
                ("product_name", models.CharField(max_length=50)),
                ("product_id", models.IntegerField()),
                ("price", models.IntegerField()),
                ("discount", models.IntegerField()),
                ("product_description", models.TextField()),
            ],
        ),
    ]