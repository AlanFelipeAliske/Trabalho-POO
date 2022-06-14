
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from core.models import Veiculos


def index(request):
    descricaoVeiculo = Veiculos.objects.get(id=1)
    response = {'descricaoVeiculo': descricaoVeiculo}
    return render(request, 'index.html', response)