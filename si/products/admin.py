from django.contrib import admin
from products.models import Product


@admin.register(Product)
class product_admin(admin.ModelAdmin):
    list_display = ['name','price','category','description','stock']


