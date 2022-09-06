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