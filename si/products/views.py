from django.shortcuts import render, redirect
from products.models import Product
from products.forms import FormularioProducts


def create_product(request):
    if request.method == 'POST':
     form= FormularioProducts(request.POST, request.FILES)

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
     form = FormularioProducts
     context = {'form':form}
     return render(request, "products/create_product.html", context=context)
   
def list(request):
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
        products.delete(products)
        return redirect(list)

def update_product(request, pk):
    if request.method == 'POST':
        form = FormularioProducts(request.POST)
        if form.is_valid():
            products = Product.objects.get(id=pk)
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            Product.stock = form.cleaned_data['stock']
            Product.save()
            return redirect(list)


    elif request.method == 'GET':
        products = Product.objects.get(id=pk)

        form = FormularioProducts(initial={
                                        'name':Product.name,
                                        'category':Product.category,
                                        'price':Product.price, 
                                        'description':Product.description,
                                        'stock':Product.stock})
        context = {'form':form}
        return render(request, 'products/update_product.html', context=context)