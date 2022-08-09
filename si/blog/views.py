from multiprocessing import context
from re import A
from django.shortcuts import render
from blog.models import article
from blog.forms import fomrularios_blog

# Create your views here.

def create_article(request):
    if request.method == 'POST':
     print(request.POST)
     new_article = article.objects.create(
        title = "Guia del barbaro",
        body = "si",
        author = "El Chascuas")
     context = {
        "new_article": new_article
     }
    elif request.method == 'GET':
     form_blog = fomrularios_blog
     context = {'form_blog':form_blog}
     return render(request, "articles/new_article.html", context=context)

def articles(request):
    articles= article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)

