from re import A
from django.shortcuts import render, redirect
from blog.models import Article
from blog.forms import FormularioBlog
from django.contrib.auth.decorators import login_required


@login_required
def create_article(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form= FormularioBlog(request.POST)

    if request.method == 'POST':
     form= FormularioBlog(request.POST, request.FILES)


    if form.is_valid():
                Article.objects.create(
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body'],
                author = form.cleaned_data['author']
                )     
                return redirect(articles)
    
    elif request.method == 'GET':
            form_blog = FormularioBlog
            context = {'form_blog':form_blog}
            return render(request, "articles/create_article.html", context=context)
    return redirect("login")

def articles(request):
    articles= Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/articles.html", context=context)

def delete_article(request, pk):
    if request.method == 'GET':
        articles = Article.objects.get(pk=pk)
        context = {'articles':articles}
        return render(request, 'articles/delete_article.html',context=context)
    elif request.method == 'POST':
        articles = Article.objects.get(pk=pk)
        Article.delete()
        return redirect(articles)

def update_article(request, pk):
    if request.method == 'POST':
        form = FormularioBlog(request.POST)
        if form.is_valid():
            articles = Article.objects.get(id=pk)
            Article.title = form.cleaned_data['title']
            Article.body = form.cleaned_data['body']
            Article.author = form.cleaned_data['author']
            Article.save()
            return redirect(articles)


    elif request.method == 'GET':
        articles = Article.objects.get(id=pk)

        form = FormularioBlog(initial={
                                        'title':Article.title,
                                        'body':Article.body,
                                        'author':Article.author})
        context = {'form':form}
        return render(request, 'articles/update_article.html', context=context)
