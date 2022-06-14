

from django.contrib import admin
from core.models import Usuarios, Veiculos, EquipamentoSeguraca, CheckList

#------------------------------------------------------------------------------

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'cpf', 'email',)
    list_filter = ('id','nome', 'cpf', 'email',)
    ordering = ('id' , 'nome', 'email')
admin.site.register(Usuarios, UsuariosAdmin)


#------------------------------------------------------------------------------

class VeiculosAdmin(admin.ModelAdmin):
    list_display = ('descricaoVeiculo',)
    list_filter = ('descricaoVeiculo',)

admin.site.register(Veiculos, VeiculosAdmin)

#------------------------------------------------------------------------------

class EquipamentoSeguracaAdmin(admin.ModelAdmin):
    list_display = ('descricaoEquipamentoSeguranca',)
    list_filter = ('descricaoEquipamentoSeguranca',)

admin.site.register(EquipamentoSeguraca, EquipamentoSeguracaAdmin)

#------------------------------------------------------------------------------

class CheckListAdmin(admin.ModelAdmin):
    list_display = ('veiculos', 'usuario',)
    list_filter = ('veiculos', 'usuario',)

admin.site.register(CheckList, CheckListAdmin)

#------------------------------------------------------------------------------
