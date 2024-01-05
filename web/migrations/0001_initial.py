# Generated by Django 5.0 on 2023-12-20 06:14

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(blank=True, max_length=120, null=True)),
                ("slug", models.SlugField(blank=True, max_length=100, unique=True)),
                ("image", models.ImageField(upload_to="blog-images/")),
                ("content", tinymce.models.HTMLField()),
                ("date", models.DateField()),
            ],
            options={
                "verbose_name": "Blog",
                "verbose_name_plural": "Blogs",
            },
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=120)),
                ("timestamp", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(blank=True, max_length=120, null=True)),
                ("subject", models.CharField(blank=True, max_length=120, null=True)),
                ("message", models.TextField()),
            ],
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=100, unique=True)),
                ("image", models.ImageField(upload_to="products/")),
                ("size", models.CharField(blank=True, max_length=120, null=True)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
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
                ("name", models.CharField(blank=True, max_length=150, null=True)),
                ("position", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="testimonial-images"
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Testimonial",
                "verbose_name_plural": "Testimonials",
            },
        ),
        migrations.CreateModel(
            name="Enquiry",
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
                ("name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.product"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductEnquiry",
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
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=120)),
                ("message", models.CharField(max_length=900)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web.product"
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Enquiry",
                "verbose_name_plural": "Product Enquiries",
            },
        ),
    ]
