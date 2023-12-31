# Generated by Django 4.2.7 on 2023-12-02 21:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Images",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("link", models.CharField(max_length=1000)),
            ],
            options={
                "abstract": False,
            },
        ),
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=500)),
                ("article", models.CharField(default="", max_length=10)),
                ("description", models.CharField(max_length=5000)),
                (
                    "product_type",
                    models.CharField(
                        choices=[
                            ("foods", "foods"),
                            ("dishes", "dishes"),
                            ("clothing", "clothing"),
                        ],
                        max_length=50,
                    ),
                ),
                ("price", models.IntegerField(default=0)),
                ("quantity", models.IntegerField(default=0)),
                ("images", models.ManyToManyField(blank=True, to="products.images")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
