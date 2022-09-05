from multiprocessing import context
from re import A
from django.shortcuts import render, redirect
from blog.models import article
from blog.forms import fomrularios_blog
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_article(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= fomrularios_blog(request.POST)

    if request.method == 'POST':
     form= fomrularios_blog(request.POST, request.FILES)


    if form.is_valid():
                article.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                author = form.cleaned_data['author']
                )     
                return redirect(articles)
    
    elif request.method == 'GET':
            form_blog = fomrularios_blog
            context = {'form_blog':form_blog}
            return render(request, "articles/new_article.html", context=context)
    return redirect("login")

def articles(request):
    articles= article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)

