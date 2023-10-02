from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.show_product, name='show_product'),
]

