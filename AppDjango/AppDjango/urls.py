
from core import views
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('usuario/', views.usuario, name='usuario'),
    path('checklist/', views.checklist, name='checklist'),
    path('checklist/detalhes/', views.detalhes, name='detalhes'),
    path('veiculos/', views.veiculos, name='veiculos'),
    path('equipamentos/', views.equipamentos, name='equipamentos'),

]
