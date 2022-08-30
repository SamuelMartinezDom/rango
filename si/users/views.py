from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {"message":f"Bienvenido al Gremio Adventure {username}"}
                return render(request, "index.html", context=context)

        form = AuthenticationForm()
        return render(request, "users/login.html", {"error": "Hubo un erorr, no estas registrado en el gremio", "form": form})

    elif request.method == "GET":
        form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})
