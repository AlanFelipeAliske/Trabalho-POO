
from django.db import models
from django.contrib.auth.models import User


class Usuarios(models.Model):
    nome = models.CharField(verbose_name = "Nome", max_length=40, blank=False, null=False)
    cpf = models.CharField(verbose_name="CPF", max_length=100, blank=True, unique=True)
    email = models.EmailField(verbose_name="Email", max_length=50, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Veiculos(models.Model):
    descricaoVeiculo = models.CharField(verbose_name="Descrição do Veículo", max_length=200, blank=False, null=False)

class EquipamentoSeguraca(models.Model):
    descricaoEquipamentoSeguranca = models.CharField(verbose_name="Descrição do Equipamento de Segurança", max_length=200, blank=True, null=True)

class CheckList(models.Model):
    equipamentoseguranca = models.ManyToManyField(EquipamentoSeguraca)
    veiculos = models.ForeignKey(Veiculos, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)