# Create your models here.

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='Нет описания')


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='Нет описания')
    image = models.ImageField(upload_to='product_images/', default='default_image.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)  # Дата создания будет автоматически заполняться при создании объекта
    updated_at = models.DateTimeField(default=timezone.now)  # Дата последнего изменения будет автоматически обновляться при сохранении объекта

    def __str__(self):
        return self.name

