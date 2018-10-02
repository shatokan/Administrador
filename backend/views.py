from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .forms import RegistrarForm,LoginForm,BicicletaForm,UsuarioForm,RoboForm,TransferenciaForm,AceptarTransferenciaForm
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings




def registrar(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistrarForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user, created = User.objects.get_or_create(username=form.cleaned_data.get('email'))
            user.email = form.cleaned_data.get('email')
            user.is_active = True
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponseRedirect(reverse('escritorio'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrarForm()

    return render(request, 'registrar.html', {'form': form})


def login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data.get('email'), password=form.cleaned_data.get('password'))
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('escritorio'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def bicicletas_agregar(request,id=None):
    # if this is a POST request we need to process the form data
    instance = Bicicleta.objects.get(pk=id) if id is not None else Bicicleta()

    if request.method == 'POST':

        if request.POST.get('Save') is not None:
            # create a form instance and populate it with data from the request:
            form = BicicletaForm(request.POST, request.FILES, instance=instance)
            # check whether it's valid:
            if form.is_valid():
                bicicleta = form.save(commit=False)
                bicicleta.usuario = request.user
                bicicleta.save()
                return HttpResponseRedirect(reverse('escritorio'))
        if request.POST.get('Delete') is not None:
            instance.delete()
            return HttpResponseRedirect(reverse('bicicletas'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BicicletaForm(instance=instance)

    action = reverse('bicicletas-agregar',args=[id] if id is not None else [])
    return render(request, 'bicicletas-agregar.html', {'form': form,'action':action})

@login_required
def bicicletas_editar(request):
    template = loader.get_template('bicicletas-editar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

@login_required
def bicicletas_eliminar(request):
    template = loader.get_template('bicicletas-eliminar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

@login_required
def bicicletas(request):
    bikes = Bicicleta.objects.filter(usuario=request.user)
    return render(request, 'bicicletas.html', {'bikes': bikes})

@login_required
def escritorio(request):
    template = loader.get_template('escritorio.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

@login_required
def datos_usuario(request):
    # if this is a POST request we need to process the form data
    instance = Usuario.objects.get(usuario=request.user) if Usuario.objects.filter(usuario=request.user).count() == 1 else Usuario()

    if request.method == 'POST':

        form = UsuarioForm(request.POST, instance=instance)
        # check whether it's valid:
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.usuario = request.user
            usuario.save()
            return HttpResponseRedirect(reverse('escritorio'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UsuarioForm(instance=instance)

    return render(request, 'datos-usuario.html', {'form': form})

@login_required
def denunciar_robo(request):

    if request.method == 'POST':

        form = RoboForm(request.user,request.POST)
        # check whether it's valid:
        if form.is_valid():

            return render(request, 'informe-robo.html', {
                'bicicletas': Bicicleta.objects.filter(id__in=form.cleaned_data.get('bicicletas')),
                'descripcion':form.cleaned_data.get('descripcion'),
                'usuario':Usuario.objects.get(usuario=request.user) if Usuario.objects.filter(usuario=request.user).count() == 1 else None,
                'url_base':settings.MEDIA_URL
                })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoboForm(request.user)

    return render(request, 'informar-robo-form.html', {'form': form})

@login_required
def transferir(request):
    if request.method == 'POST':

        form = TransferenciaForm(request.user,request.POST)
        # check whether it's valid:
        if form.is_valid():
            transferencia = form.save(commit=False)
            transferencia.usuario_desde = request.user
            transferencia.save()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TransferenciaForm(request.user)

    return render(request, 'transferir.html', {'form': form})

@login_required
def transferencias(request,id=None):

    return render(request, 'transferencias.html', {'transferencias': Transferencia.objects.filter(usuario_hacia=request.user)})


@login_required
def transferencia(request,id):
    transferencia = Transferencia.objects.get(pk=id)
    if request.method == 'POST':

        form = AceptarTransferenciaForm(request.user,request.POST)
        # check whether it's valid:
        if form.is_valid():
            if request.POST.get('Save') is not None:
                transferencia.estado = Transferencia.ACEPTADO
                transferencia.bicicleta.usuario = request.user
                transferencia.bicicleta.save()
                transferencia.save()
                
                return HttpResponseRedirect(reverse('bicicletas'))

            if request.POST.get('Delete') is not None:
                transferencia.estado = Transferencia.RECHAZADO
                transferencia.save()
                return HttpResponseRedirect(reverse('transferencias',args=[transferencia.id]))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AceptarTransferenciaForm(request.user,initial={'transferencia': id})

    return render(request, 'transferencia.html', {'form': form,'transferencia':transferencia, 'url_base':settings.MEDIA_URL})



def recuperar(request):
    template = loader.get_template('recuperar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))