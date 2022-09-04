from http.client import HTTPResponse
from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from products.models import product
from products.forms import fomrularios_productos
from django.contrib.auth.decorators import login_required



def create_product(request):
#<<<<<<< HEAD
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= fomrularios_productos(request.POST)
#=======
    if request.method == 'POST':
     form= fomrularios_productos(request.POST, request.FILES)
#>>>>>>> 508f93e2263bdf028e8cbe66a9b9a56eeae4b6fa

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
    return redirect("login")

@login_required
def list(request):
    products = product.objects.all()
    context = {"products": products}
    return render(request, "products/list.html", context=context)

@login_required
def search_products(request):
   search = request.GET['search']
   products = product.objects.filter(name__icontains=search)
   context={'products':products}
   return render(request, 'products/search_products.html', context=context)
