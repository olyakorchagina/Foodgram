import csv

from django.conf import settings
from django.core.management import BaseCommand

from recipes.models import Ingredient, Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data_path = settings.BASE_DIR
        with open(
            data_path / 'data/ingredients.csv', 'r', encoding='utf-8'
        ) as file:
            reader = csv.DictReader(file)
            Ingredient.objects.bulk_create(
                Ingredient(**data) for data in reader
            )

        data = [
            {'name': 'Завтрак', 'color': '#F79707', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#38B519', 'slug': 'lunch'},
            {'name': 'Ужин', 'color': '#613BF7', 'slug': 'dinner'},
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)

        self.stdout.write(self.style.SUCCESS('Successfully load data'))
