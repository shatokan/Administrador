"""bicicletas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from backend.views import registrar,bicicletas_agregar,bicicletas_editar,bicicletas_eliminar,bicicletas,escritorio,datos_usuario,login,recuperar,denunciar_robo,transferir,transferencias,transferencia,reporte_robo



urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar',registrar,name="registrar"),
    path('bicicletas-agregar',bicicletas_agregar,name="bicicletas-agregar"),
    path('bicicletas-agregar/<int:id>/',bicicletas_agregar,name="bicicletas-agregar"),
    path('bicicletas-editar',bicicletas_editar,name="bicicletas-editar"),
    path('bicicletas_eliminar',bicicletas_eliminar,name="bicicletas-eliminar"),
    path('bicicletas',bicicletas,name="bicicletas"),
    path('escritorio',escritorio,name="escritorio"),
    path('datos_usuario',datos_usuario,name='datos-usuario'),
    path('login',login,name="login"),
    path('recuperar',recuperar,name="recuperar"),
    path('denunciar-robo',denunciar_robo,name="denunciar-robo"),
    path('reporte-robo/<int:id>/',reporte_robo,name="reporte-robo"),
    path('transferir',transferir,name="transferir"),
    path('transferencias',transferencias,name="transferencias"),
    path('transferencias/<int:id>/',transferencias,name="transferencias"),
    path('transferencia/<int:id>/',transferencia,name="transferencia"),
    #path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
