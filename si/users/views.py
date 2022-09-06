from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegistrationForm
from users.models import UserProfile

def login_request(request):
    """Esta vista retorna el inicio sesion mediante un formulario, 
    requiere que ingrese un usuario valido que haya sido registrado anteriormente, 
    ademas de que no requiere estar logueado ni ser admin para acceder."""
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {"message":f"¿Listo para tu proxima campaña? {username}"}
                return render(request, "index.html", context=context)

        form = AuthenticationForm()
        return render(request, "users/login.html", {"error": "Hubo un erorr, no estas registrado en el gremio", "form": form})

    elif request.method == "GET":
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def register(request):
    """Esta vista retorna el usuario creado por medio un formulario, 
    esta vista no requiere estar logueado ni ser admin para acceder"""
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context = {"errors": form.errors}
            form = User_registration_form
            context["form"] = form
            return render(request, "users/register.html", context)
    elif request.method == "GET":
        form = UserRegistrationForm()
        return render(request, "users/register.html", {"form": form})
