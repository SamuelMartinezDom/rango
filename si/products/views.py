from http.client import HTTPResponse
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from products.models import Product
from products.forms import FormulariosProduct


# Create your views here.

def create_product(request):
    if request.method == 'POST':
     form= fo(request.POST, request.FILES)

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
     form = fomrularios_productos
     context = {'form':form}
     return render(request, "products/create_product.html", context=context)
   
def list(request):
    products = Product.objects.all()
    """Esta vista retorna el producto creado mediante un formulario, 
    ademas requiere estar logueado y ser admin para acceder, sino te envia al registro."""
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

@login_required
def list(request):
    """Esta vista retorna todos los productos de la base de datos y los muestra, 
    ademas requiere estar logueado, sino te manda al registro"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products/list.html", context=context)

def search_products(request):
   search = request.GET['search']
   products = Product.objects.filter(name__icontains=search)
   context={'products':products}
   return render(request, 'products/search_products.html', context=context)

def delete_product(request, pk):
    if request.method == 'GET':
        products = Product.objects.get(pk=pk)
        context = {'Product':products}
        return render(request, 'products/delete_product.html',context=context)
    elif request.method == 'POST':
        products = Product.objects.get(pk=pk)
        products.delete()
        return redirect(list)

def update_product(request, pk):
    if request.method == 'POST':
        form = fomrularios_productos(request.POST)
        if form.is_valid():
            products = Product.objects.get(id=pk)
            Product.name = form.cleaned_data['name'],
            Product.category = form.cleaned_data['category'],
            Product.description = form.cleaned_data['description'],
            Product.price = form.cleaned_data['price'],
            Product.stock = form.cleaned_data['stock']
            Product.save()
            return redirect(list)


    elif request.method == 'GET':
        products = Product.objects.get(id=pk)

        form = fomrularios_productos(initial={
                                        'name':Product.name,
                                        'category':Product.category,
                                        'price':Product.price, 
                                        'description':Product.description,
                                        'stock':Product.stock})
        context = {'form':form}
        return render(request, 'products/update_product.html', context=context)
    """Esta vista retorna los productos que buscaste mediante un filtro y los muestra, 
    ademas requiere estar logueado, sino te manda al registro"""
    search = request.GET['search']
    products = Product.objects.filter(name__icontains=search)
    context={'products':products}
    return render(request, 'products/search_products.html', context=context)
