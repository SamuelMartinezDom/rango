
from django.contrib import admin
from django.urls import path
from products.views import list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list/", list, name= "list")
]
