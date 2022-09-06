from re import A
from django.shortcuts import render, redirect
from blog.models import Article
from blog.forms import FormulariosBlog
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_article(request):
    """Esta vista retorna el articulo creado, 
    ademas requiere estar logueado y ser admin para acceder, de lo contrario te envia al registro."""
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= FormulariosBlog(request.POST)

    if request.method == 'POST':
     form= FormulariosBlog(request.POST, request.FILES)


    if form.is_valid():
                Article.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                author = form.cleaned_data['author']
                )     
                return redirect(articles)

    elif request.method == 'GET':
            form_blog = FormulariosBlog
            context = {'form_blog':form_blog}
            return render(request, "articles/new_article.html", context=context)
    return redirect("login")

@login_required
def articles(request):
    """Esta vista retorna todos los articulos de la base de datos y los muestra, 
    ademas requiere estar logueado, sino te manda al registro"""
    articles= Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)
