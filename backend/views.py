from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404


def registrar(request):
    template = loader.get_template('Registrar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def bicicletas_agregar(request):
    template = loader.get_template('bicicletas-agregar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def bicicletas_editar(request):
    template = loader.get_template('bicicletas-editar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def bicicletas_eliminar(request):
    template = loader.get_template('bicicletas-eliminar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def bicicletas(request):
    template = loader.get_template('bicicletas.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def escritorio(request):
    template = loader.get_template('escritorio.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def formulario_de_registro(request):
    template = loader.get_template('formulario-de-registro.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

def recuperar(request):
    template = loader.get_template('recuperar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))