from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from jaguarete.models import Cart


class RegistroForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(
        attrs={            
            'class': 'form-control',
        }
    ))
    password1 = forms.CharField(label='Contraseña', widget=forms.TextInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'id': 'password1'
        }
    ))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.TextInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'id': 'password2'
        }
    ))
    
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'id': 'email'
        }
    ))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')