from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from .models import Account
from .forms import AccountForm

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


class AccountCreateView(CreateView):
    model = Account
    template_name = "account/register.html"
    form_class = AccountForm

    def form_valid(self, form):
        data = form.cleaned_data        
        account = Account.objects.create(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            password=make_password(form.cleaned_data['confirm_password']),
            type_user=form.cleaned_data['type_user'],
            email=form.cleaned_data['email'],
            is_active=False)

        messages.success(self.request, "Cadastro realizado com sucesso!")            
            
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('account:signin')
