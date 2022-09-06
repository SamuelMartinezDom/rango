from django.urls import path
from products.views import create_product, list, search_products, delete_product, update_product


urlpatterns = [
    path("list/", list, name= "list"),
    path('create_product/', create_product, name= 'create_product'),
    path('search_products/', search_products, name='search_products'), 
    path('delete_product/<int:pk>/', delete_product, name='delete_product'),
    path('update_product/<int:pk>/', update_product, name='update_product'),
]
