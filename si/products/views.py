from multiprocessing import context
from django.shortcuts import render
from products.models import product

# Create your views here.

def create_product(request):
    new_product = product.objects.create(
        name = "Esmeralda",
        parentesco = "Hermana",
        age = 6,
        date_of_birth = "22/22/22")
    context = {
        "new_product": new_product
    }
    return render(request, "new_product.html", context=context)

def list(request):
    products = product.objects.all()
    context = {"products": products}
    return render(request, "list.html", context=context)