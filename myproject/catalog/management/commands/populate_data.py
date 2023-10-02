from django.core.management.base import BaseCommand
from ...models import Category, Product
import json



class Command(BaseCommand):
    help = 'Populate database with data from fixtures'

    def handle(self, *args, **kwargs):
        # Очистка данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загрузка данных из фикстур
        with open('fixtures.json') as f:
            data = json.load(f)

        # Вставка данных из фикстур
        categories = {}
        for obj in data:
            model = obj['model']
            fields = obj['fields']

            if model == 'myapp.category':
                category = Category.objects.create(name=fields['name'])
                categories[fields['pk']] = category
            elif model == 'myapp.product':
                category = categories[fields['category']]
                Product.objects.create(name=fields['name'], category=category, price=fields['price'])

        self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
