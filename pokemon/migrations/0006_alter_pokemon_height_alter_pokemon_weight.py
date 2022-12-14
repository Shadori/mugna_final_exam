# Generated by Django 4.1.2 on 2022-10-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon", "0005_rename_name_pokemontype_element_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pokemon",
            name="height",
            field=models.DecimalField(
                decimal_places=2, max_digits=20, verbose_name="Height (in meters)"
            ),
        ),
        migrations.AlterField(
            model_name="pokemon",
            name="weight",
            field=models.DecimalField(
                decimal_places=2, max_digits=20, verbose_name="Weight (in kilograms)"
            ),
        ),
    ]
