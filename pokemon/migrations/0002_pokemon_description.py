# Generated by Django 4.1.2 on 2022-10-27 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemon",
            name="description",
            field=models.TextField(default="Pokemon description unavailable"),
        ),
    ]