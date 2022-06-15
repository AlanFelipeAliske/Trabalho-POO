
from collections import UserList
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Veiculos, AuthUser


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
            return redirect('/inicio/')
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

def index(request):
    #email = Usuarios.objects.get(id=1)
    #response = {'email': email}
    return render(request, 'index.html')

# ----------------------------------------------------------------

@login_required(login_url='/login/')
def usuario(request):
    id = request.user.id
    username = request.user
    email = request.user.email
    response = {'id': id, 'username': username, 'email': email}
    return render(request, 'usuario.html', response)

# ----------------------------------------------------------------

def equipamentos(request):
    return render(request, 'equipamentos.html')

# ----------------------------------------------------------------

def veiculos(request):
    veiculo = Veiculos.objects.all()
    response = {'veiculos': veiculo}
    return render(request, 'veiculos.html', response)

# ----------------------------------------------------------------

def checklist(request):
    return render(request, 'checklist.html')

# ----------------------------------------------------------------

# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------


# ----------------------------------------------------------------

