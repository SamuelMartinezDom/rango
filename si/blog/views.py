from multiprocessing import context
from re import A
from django.shortcuts import render
from blog.models import article

# Create your views here.

def create_article(request):
    new_article = article.objects.create(
        title = "Guia del barbaro",
        body = "si",
        author = "El Chascuas")
    context = {
        "new_article": new_article
    }
    return render(request, "articles/new_article.html", context=context)

def articles(request):
    articles= article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)