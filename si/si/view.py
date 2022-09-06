from django.shortcuts import render


def index(request):
    """Esta vista retorna el index de la pagina"""
    return render(request, "index.html")


def about_us(request):
    """Esta vista retorna la pestaña con nustra informacion"""
    return render(request, "about_us.html")