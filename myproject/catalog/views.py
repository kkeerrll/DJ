from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from .models import Product

def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product
    except Product.DoesNotExist:
        return None

def show_product(request, product_id):
    # Получение информации о товаре с помощью переданного идентификатора (product_id)
    product = get_product_by_id(product_id)

    # Отображение шаблона с переданными данными о товаре
    return render(request, 'product.html', {'product': product})
