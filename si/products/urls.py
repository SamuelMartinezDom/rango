from django.urls import path
from products.views import create_product, list, search_products


urlpatterns = [
    path("list/", list, name= "list"),
    path('create_product/', create_product, name= 'create_product'),
    path('search_products/', search_products, name='search_products')
]
