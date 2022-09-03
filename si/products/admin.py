from django.contrib import admin
from products.models import product
# Register your models here.

@admin.register(product)
class product_admin(admin.ModelAdmin):
    list_display = ['name','price','category','description','stock']


