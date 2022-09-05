from http.client import HTTPResponse
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from products.models import Product
from products.forms import FormulariosProduct
from django.contrib.auth.decorators import login_required



def create_product(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= FormulariosProduct(request.POST, request.FILES)


    if form.is_valid():
        Product.objects.create(
        name = form.cleaned_data['name'],
        category = form.cleaned_data['category'],
        description = form.cleaned_data['description'],
        price = form.cleaned_data['price'],
        stock = form.cleaned_data['stock']
        )     
        return redirect(list)

    elif request.method == 'GET':
        form = FormulariosProduct
        context = {'form':form}
        return render(request, "products/create_product.html", context=context)
    return redirect("login")

@login_required
def list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/list.html", context=context)

@login_required
def search_products(request):
   search = request.GET['search']
   products = Product.objects.filter(name__icontains=search)
   context={'products':products}
   return render(request, 'products/search_products.html', context=context)
