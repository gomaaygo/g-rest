from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.views.generic.detail import DetailView
from django.views.decorators.csrf import csrf_exempt

from .models import Account
from .forms import AccountForm

# Create your views here.

@csrf_exempt
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
        super().form_valid(form)

        if self.object.type_user == "cashier":
            group = get_object_or_404(Group, name="Caixa")
        elif self.object.type_user == "waiter":
            group = get_object_or_404(Group, name="Garçom")
        else:
            group = get_object_or_404(Group, name="Gerente")

        self.object.password = make_password(self.request.POST["password"])
        self.object.groups.add(group)
        self.object.save()

        messages.success(self.request, "Cadastro realizado com sucesso!")            
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('account:signin')


class EditAccountView(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ['first_name', 'last_name', 'username', 'email']
    template_name = 'account/edit_account.html'

    def get_success_url(self):
        messages.success(self.request, "Conta atualizada com sucesso!")  
        return reverse('core:index')


class NewPasswordView(LoginRequiredMixin, PasswordChangeView, TemplateView):
    template_name = 'account/new_password.html'
    success_url = reverse_lazy('account:signin')

    def form_valid(self, form):
        messages.success(
            self.request, "Senha atualizada com sucesso!")
        logout(self.request)
        return super().form_valid(form)


class AccountDetailView(DetailView):
    model = Account

    def get_account(self):
        return Account.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_account()
        return context