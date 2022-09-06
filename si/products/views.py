from http.client import HTTPResponse
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from products.models import product
from products.forms import fomrularios_productos


# Create your views here.

def create_product(request):
    if request.method == 'POST':
     form= fomrularios_productos(request.POST, request.FILES)

     if form.is_valid():
            product.objects.create(
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
    products = product.objects.all()
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
   products = product.objects.filter(name__icontains=search)
   context={'products':products}
   return render(request, 'products/search_products.html', context=context)

def delete_product(request, pk):
    if request.method == 'GET':
        products = product.objects.get(pk=pk)
        context = {'product':products}
        return render(request, 'products/delete_product.html',context=context)
    elif request.method == 'POST':
        products = product.objects.get(pk=pk)
        products.delete()
        return redirect(list)

def update_product(request, pk):
    if request.method == 'POST':
        form = fomrularios_productos(request.POST)
        if form.is_valid():
            products = product.objects.get(id=pk)
            product.name = form.cleaned_data['name'],
            product.category = form.cleaned_data['category'],
            product.description = form.cleaned_data['description'],
            product.price = form.cleaned_data['price'],
            product.stock = form.cleaned_data['stock']
            product.save()
            return redirect(list)


    elif request.method == 'GET':
        products = product.objects.get(id=pk)

        form = fomrularios_productos(initial={
                                        'name':product.name,
                                        'category':product.category,
                                        'price':product.price, 
                                        'description':product.description,
                                        'stock':product.stock})
        context = {'form':form}
        return render(request, 'products/update_product.html', context=context)
    """Esta vista retorna los productos que buscaste mediante un filtro y los muestra, 
    ademas requiere estar logueado, sino te manda al registro"""
    search = request.GET['search']
    products = Product.objects.filter(name__icontains=search)
    context={'products':products}
    return render(request, 'products/search_products.html', context=context)
