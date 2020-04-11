from django import forms
from .models import *

class UserForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['NombreUsuario', 'Contrasenya', 'Correo', 'FotoDePerfil']

class AudioForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = ['FicheroDeAudio', 'Titulo', 'Idioma', 'Duracion']