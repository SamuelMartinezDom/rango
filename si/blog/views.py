from re import A
from django.shortcuts import render, redirect
from blog.models import Article
from blog.forms import FormularioBlog
from django.contrib.auth.decorators import login_required


@login_required
def create_article(request):
    """Esta vista retorna el articulo creado, 
    ademas requiere estar logueado y ser admin para acceder, de lo contrario te envia al registro."""
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= FormularioBlog(request.POST, request.FILES)


        if form.is_valid():
                Article.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                author = form.cleaned_data['author'])     
                return redirect(articles)
    
    elif request.method == 'GET':
            form_blog = FormularioBlog
            context = {'form_blog':form_blog}
            return render(request, "articles/create_article.html", context=context)
    return redirect("login")


@login_required
def articles(request):
    """Esta vista retorna todos los articulos de la base de datos y los muestra, 
    ademas requiere estar logueado, de lo contrario te manda al registro"""
    articles= Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)


@login_required
def delete_article(request, pk):
    """Esta vista retorna un delete del personaje que seleccionaste, 
    ademas requiere estar logueado y ser admin para acceder, sino te manda al registro"""
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            article = Article.objects.get(pk=pk)
            context = {'article':article}
            return render(request, 'articles/delete_article.html',context=context)
        elif request.method == 'POST':
            article = Article.objects.get(pk=pk)
            Article.delete(article)
            return redirect(articles)


@login_required
def update_article(request, pk):
    """Esta vista retorna un update del articulo que seleccionaste, 
    ademas requiere estar logueado y ser admin para acceder, sino te manda al registro"""
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = FormularioBlog(request.POST)
            if form.is_valid():
                article =  Article.objects.get(id=pk)
                article.title = form.cleaned_data['title']
                article.body = form.cleaned_data['body']
                article.author = form.cleaned_data['author']
                article.save()
                return redirect(articles)


        elif request.method == 'GET':
            article = Article.objects.get(id=pk)
            form = FormularioBlog(initial={
                                        'title':article.title,
                                        'body':article.body,
                                        'author':article.author})
            context = {'form':form}
            return render(request, 'articles/update_article.html', context=context)
