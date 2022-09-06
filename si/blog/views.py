from multiprocessing import context
from re import A
from django.shortcuts import render, redirect
from blog.models import article
from blog.forms import FormulariosBlog
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_article(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= FormulariosBlog(request.POST)

    if request.method == 'POST':
     form= FormulariosBlog(request.POST, request.FILES)


    if form.is_valid():
                article.objects.create(
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

def articles(request):
    articles= article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)

def delete_article(request, pk):
    if request.method == 'GET':
        articles = article.objects.get(pk=pk)
        context = {'articles':articles}
        return render(request, 'articles/delete_article.html',context=context)
    elif request.method == 'POST':
        articles = article.objects.get(pk=pk)
        article.delete()
        return redirect(articles)

def update_article(request, pk):
    if request.method == 'POST':
        form = FormulariosBlog(request.POST)
        if form.is_valid():
            articles = article.objects.get(id=pk)
            article.title = form.cleaned_data['title'],
            article.body = form.cleaned_data['body'],
            article.author = form.cleaned_data['author']
            article.save()
            return redirect(articles)


    elif request.method == 'GET':
        articles = article.objects.get(id=pk)

        form = FormulariosBlog(initial={
                                        'title':article.title,
                                        'body':article.body,
                                        'author':article.author})
        context = {'form':form}
        return render(request, 'articles/update_article.html', context=context)
