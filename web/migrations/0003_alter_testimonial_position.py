# Generated by Django 5.0 on 2023-12-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_alter_testimonial_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="position",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
