from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,Http404
from .forms import RegistrarForm,LoginForm,BicicletaForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required




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
            return HttpResponseRedirect('/escritorio')

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
                return HttpResponseRedirect('/escritorio')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required
def bicicletas_agregar(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BicicletaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/escritorio')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BicicletaForm()

    return render(request, 'bicicletas-agregar.html', {'form': form})

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
    template = loader.get_template('bicicletas.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

@login_required
def escritorio(request):
    template = loader.get_template('escritorio.html')
    context = dict({})
    return HttpResponse(template.render(context, request))

@login_required
def formulario_de_registro(request):
    template = loader.get_template('formulario-de-registro.html')
    context = dict({})
    return HttpResponse(template.render(context, request))


def recuperar(request):
    template = loader.get_template('recuperar.html')
    context = dict({})
    return HttpResponse(template.render(context, request))