from sqlite3 import ProgrammingError, IntegrityError

from django.core.management import BaseCommand, call_command
from ...models import Category, Product
import json

class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options) -> None:
        try:
            call_command('loaddata', 'fixtures.json')
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(self.style.NOTICE(f'Invalid fixtures: {e}'))
        else:
            self.stdout.write(self.style.SUCCESS(
                'Command have been completed successfully'
            ))


# class Command(BaseCommand):
#     help = 'Populate database with data from fixtures'
#
#     def handle(self, *args, **kwargs):
#         # Очистка данных
#         Category.objects.all().delete()
#         Product.objects.all().delete()
#
#         # Загрузка данных из фикстур
#         with open('fixtures.json') as f:
#             data = json.load(f)
#
#         # Вставка данных из фикстур
#         categories = {}
#         for obj in data:
#             model = obj['model']
#             fields = obj['fields']
#
#             if model == 'myapp.category':
#                 category = Category.objects.create(name=fields['name'])
#                 categories[fields['pk']] = category
#             elif model == 'myapp.product':
#                 category = categories[fields['category']]
#                 Product.objects.create(name=fields['name'], category=category, price=fields['price'])
#
#         self.stdout.write(self.style.SUCCESS('Database populated successfully.'))
