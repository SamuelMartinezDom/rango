from django.urls import path, include
from blog.views import create_article, articles

urlpatterns = [
    path("articles/", articles, name= "articles"),
]
