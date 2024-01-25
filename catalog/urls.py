from django.urls import path

from catalog.apps import MainConfig
from catalog.views import index, contacts, products, category_products, product_item

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('category_products/', category_products, name='category_products'),
    path('<int:pk>/products/', products, name='products'),
    path('contacts', contacts, name='contacts'),
    path('<int:pk>/product_item', product_item, name='product_item'),
]