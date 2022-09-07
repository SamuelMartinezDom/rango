from django.urls import path
from blog.views import create_article, articles, delete_article, update_article


urlpatterns = [
    path("articles/", articles, name= "articles"),
    path('create_article/', create_article, name= 'create_article'),
    path('delete_article/<int:id>/', delete_article, name='delete_article'),
    path('update_article/<int:id>/', update_article, name='update_article'),]
