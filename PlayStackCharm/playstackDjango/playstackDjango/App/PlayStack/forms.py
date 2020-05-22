from django import forms
from .models import *

# Las formas permiten la creación de objetos
# que contienen ficheros como campos

# Crea un usuario con una imagen como
# foto de perfil
class UserForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['NombreUsuario', 'Contrasenya', 'Correo', 'FotoDePerfil']

# Crea un audio en la base de datos
class AudioForm(forms.ModelForm):

    class Meta:
        model = Audio
        fields = ['FicheroDeAudio', 'Titulo', 'Idioma', 'Duracion', 'CreadorDeContenido']

# Crea un album en la base de datos
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['NombreAlbum', 'Fecha', 'FotoDelAlbum']

class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['Nombre', 'Descripcion', 'Tematica','FotoDelPodcast']