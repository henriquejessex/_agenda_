from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Evento

# Create your views here.


def user_login(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        # pegando os dados do input html
        username = request.POST.get('username')
        password = request.POST.get('password')

        # autenticando
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha inválido.")
    return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):

    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        # pegando os dados do evento.html
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              data_evento=data_evento,
                              descricao=descricao,
                              usuario=usuario)
    return redirect('/')


# def index(request):
#    return redirect('/agenda/')
