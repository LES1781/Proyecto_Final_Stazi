from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from vhsApp.models import Avatar


class CassetteFormulario(forms.Form):

    nombre = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=200)
    año = forms.CharField(max_length=4)
    descripcion = forms.CharField(max_length=300)


class MembresiaFormulario(forms.Form):

    nombre = forms.CharField(max_length=200)
    precio = forms.DecimalField(max_digits=5, decimal_places=2)
    Facturacion = forms.CharField(max_length=20)


class SolicitudFormulario(forms.Form):

    solicitud = forms.CharField(max_length=500)
    fecha = forms.CharField(max_length=30)


class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(
                                label='Contraseña',
                                widget=forms.PasswordInput
                               )

    password2 = forms.CharField(
                                label='Repetir contraseña',
                                widget=forms.PasswordInput
                               )

    class Meta:

        model = User
        fields = [
                  'last_name',
                  'first_name',
                  'username',
                  'email',
                  'password1',
                  'password2'
                 ]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']
