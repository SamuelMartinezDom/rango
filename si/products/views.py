from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from products.models import product

# Create your views here.

def create_product(request):
    new_product = product.objects.create(
        name = "Dado D20",
        category = "Dados",
        price = 350,
        stock = 10)
    context = {
        "new_product": new_product
    }
    return render(request, "products/new_product.html", context=context)

def list(request):
    products = product.objects.all()
    context = {"products": products}
    return render(request, "products/list.html", context=context)