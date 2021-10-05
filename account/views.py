from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Seja bem vindo(a)!")
            return redirect('core:index')
        else:
            form = AuthenticationForm()
            messages.error(request, "Usuário ou senha incorreto! Tente novamente!")
    else:
        form = AuthenticationForm()
        
    return render(request, 'account/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('account:signin')
