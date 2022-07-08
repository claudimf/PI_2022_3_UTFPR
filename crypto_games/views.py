from crypto_games.models import Noticia
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


from .forms import SignUpForm, NoticiaForm, ServicoForm


def home(request):
    noticias = Noticia.objects.filter(tipo='P')
    contexto = {
        'noticias': noticias
    }
    return render(request, 'home.html', contexto)


@login_required(login_url='login/')
def home_privada(request):
    noticias = Noticia.objects.all()
    contexto = {
        'noticias': noticias
    }
    return render(request, 'home_privada.html', contexto)


@method_decorator(login_required(login_url='login'), name='dispatch')
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login/logout.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login/login.html')

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_page = request.GET.get('next', None)
            if next_page:
                return redirect(next_page)
            return redirect('home_privada')
        else:
            messages.error(request, "Erro! Usuário ou senha incorreta.")
            return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='login/')
def post_noticia(request):
    form = NoticiaForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = NoticiaForm()
    return render(request, "noticia/noticia_form.html", {"form": form})


@login_required(login_url='login/')
def post_servico(request):
    form = ServicoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = ServicoForm()
    return render(request, "servico/servico_form.html", {"form": form})


def noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)

    contexto = {
        'noticia': noticia
    }
    return render(request, "noticia/noticia.html", contexto)
