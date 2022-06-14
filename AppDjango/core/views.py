
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# ----------------------------------------------------------------


def login_user(request):
    return render(request, 'login.html')

# ----------------------------------------------------------------


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('inicio/')
        else:
            messages.error(request, 'Senha ou usuario invalidos')
        return redirect('/')

# ----------------------------------------------------------------


def logout_user(request):
    logout(request)
    return redirect('/')

# ----------------------------------------------------------------


def inicio(request):
    return render(request, 'inicio.html')

# ----------------------------------------------------------------

from core.models import Veiculos


def index(request):
    return render(request, 'index.html')

# ----------------------------------------------------------------


def usuarios(request):
    return render(request, 'usuarios.html')

# ----------------------------------------------------------------


def equipamentos(request):
    return render(request, 'equipamentos.html')

# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------
    descricaoVeiculo = Veiculos.objects.get(id=1)
    response = {'descricaoVeiculo': descricaoVeiculo}
    return render(request, 'index.html', response)
