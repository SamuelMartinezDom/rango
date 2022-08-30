from django.contrib import admin
from django.urls import path, include
from si.view import index

urlpatterns = [
    path("", index, name="index.html"),
    path("admin/", admin.site.urls),
    path("products/", include("products.urls")),
    path("blog/", include("blog.urls")),
    path("characters/", include("characters.urls")),
    path("users/", include("users.urls"))
]
