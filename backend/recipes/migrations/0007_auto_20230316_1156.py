# Generated by Django 3.2.18 on 2023-03-16 08:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20230310_1401'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='recipeingredient',
            name='unique_recipe_ingredient',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение: 1')], verbose_name='Время приготовления (в минутах)'),
        ),
    ]
