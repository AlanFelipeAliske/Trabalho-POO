
from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    #path('core/', include('core.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index')

]