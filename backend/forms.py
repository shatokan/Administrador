from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Bicicleta, Usuario, Transferencia, Robo


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

    remember_me = forms.BooleanField(label="Recuerdame",required=False)


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


class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['numero_serie','descripcion','factura','foto','marca','modelo','estilo','color_primario','color_secundario','aro']
        widgets = {
            'factura': forms.FileInput(),
            'foto':forms.FileInput(),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','apellido','rut','telefono','direccion','region']


class RoboForm(forms.ModelForm):

    class Meta:
        model = Robo
        fields = ['bicicletas','comuna','fecha','descripcion']
        widget = {
            'fecha':forms.DateTimeInput()
        }

    def __init__(self, user, *args, **kwargs):
        super(RoboForm, self).__init__(*args, **kwargs)
        self.fields['bicicletas'] = forms.ModelMultipleChoiceField(queryset=Bicicleta.objects.filter(usuario=user),widget=forms.CheckboxSelectMultiple())



class TransferenciaForm(forms.ModelForm):
    class Meta:
        model = Transferencia
        fields = ['usuario_hacia','bicicleta','mensaje']

    def __init__(self, user, *args, **kwargs):
        super(TransferenciaForm, self).__init__(*args, **kwargs)
        self.fields['bicicleta'] = forms.ModelChoiceField(queryset=Bicicleta.objects.filter(usuario=user))
        self.fields['usuario_hacia'] = forms.ModelChoiceField(
            queryset=User.objects.exclude(id=user.id),
            to_field_name='username',
            widget=forms.EmailInput,
            error_messages={'invalid_choice': "Usuario no fue encontrado"},
            help_text="Correo del usuario destinatario",
            label="Destinatario")

        

class AceptarTransferenciaForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(AceptarTransferenciaForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['transferencia'] = forms.ModelChoiceField(
            queryset=Transferencia.objects.filter(usuario_hacia=user),
            widget=forms.HiddenInput)




