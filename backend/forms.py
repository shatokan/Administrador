from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Bicicleta


class RegistrarForm(forms.Form):

    email = forms.EmailField(
                    min_length=4,
                    max_length=80,
                    required=True,
                    label="Correo")

    password = forms.CharField(
                    widget=forms.PasswordInput,
                    min_length=6,
                    max_length=30,
                    required=True,
                    label="Clave")

    confirm_password = forms.CharField(
                    widget=forms.PasswordInput,
                    min_length=6,
                    max_length=30,
                    required=True,
                    label="Confirme Clave")

    terms = forms.BooleanField(required=True)

    email.widget.attrs.update({'class': 'form-control form-control-lg'})
    password.widget.attrs.update({'class': 'form-control form-control-lg'})
    confirm_password.widget.attrs.update({'class': 'form-control form-control-lg'})

    def clean(self):
        cleaned_data = super(RegistrarForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Las claves no coinciden"
            )

        if User.objects.filter(username=cleaned_data.get('email')):
            raise forms.ValidationError(
                "El correo " + cleaned_data.get('email') + " ya esta registrado"
            )

        return cleaned_data

class LoginForm(forms.Form):

    email = forms.EmailField(
                    min_length=4,
                    max_length=80,
                    required=True,
                    label="Correo")
    
    password = forms.CharField(
                    widget=forms.PasswordInput,
                    min_length=6,
                    max_length=30,
                    required=True,
                    label="Clave")

    remember_me = forms.BooleanField(label="Recuerdame")


    email.widget.attrs.update({'class': 'form-control form-control-lg'})
    password.widget.attrs.update({'class': 'form-control form-control-lg'})

    def clean(self):

        cleaned_data = super(LoginForm, self).clean()

        if User.objects.filter(username=cleaned_data.get('email')).count() == 0:
            raise forms.ValidationError(
                "No existe este usuario"
            )

        user = authenticate(username=cleaned_data.get('email'), password=cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError(
                "Usuario y clave no coinciden"
            )


class BicicletaForm(ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['numero_serie','descripcion','factura','foto','marca','modelo','estilo','color_primario','color_secundario','aro']

