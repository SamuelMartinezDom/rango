from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/", include("products.urls")),
    path("blog/", include("blog.urls")),
    path("characters/", include("characters.urls"))
]
