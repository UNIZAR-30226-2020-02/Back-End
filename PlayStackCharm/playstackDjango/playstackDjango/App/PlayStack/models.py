from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from .functions import *
import binascii

# Create your models here.

class Usuario(models.Model):
    ID = models.AutoField(primary_key=True)
    NombreUsuario = models.CharField(max_length=300, null=False, unique=True)
    # USERNAME_FIELD = 'NombreUsuario'
    Contrasenya = models.CharField(max_length=300, null=False)
    # Contrasenya puede ser reemplazado por password por django
    Correo = models.CharField(max_length=300, null=False, unique=True)
    FotoDePerfil = models.ImageField(null=True, blank=True, upload_to='images')
    Seguidos = models.ManyToManyField('self', through='Relacion', blank=True, symmetrical=False,
                                      related_name='Seguidores')
    SolicitudAmistad = models.ManyToManyField('self', through='Peticiones', blank=True, symmetrical=False,
                                              related_name='Solicitudes')

    def __str__(self):

        return decrypt(binascii.unhexlify(self.NombreUsuario)).decode('ascii')

    def getFotoDePerfil(self, httphost):
        return 'https://' + httphost + settings.MEDIA_URL + self.FotoDePerfil.name

    def follow(self, user):
        relacion, created = Relacion.objects.get_or_create(
            fromUser=self,
            toUser=user)
        return relacion

    def addRequest(self, user):
        peticion, created = Peticiones.objects.get_or_create(
            fromUser=self,
            toUser=user)
        return peticion

    def unFollow(self, user):
        Relacion.objects.filter(
            fromUser=self,
            toUser=user).delete()

    def removeRequest(self, user):
        Peticiones.objects.filter(
            fromUser=self,
            toUser=user).delete()

    def getFollowing(self):
        return self.Seguidos.filter(
            to_users__fromUser=self)

    def getFollowers(self):
        return self.Seguidores.filter(
            from_users__toUser=self)
    def getRequests(self):
        return self.Solicitudes.filter(
            from_usr__toUser=self)

class Relacion (models.Model):
    fromUser = models.ForeignKey(Usuario, related_name='from_users', on_delete=models.CASCADE)
    toUser = models.ForeignKey(Usuario, related_name='to_users', on_delete=models.CASCADE)

class Peticiones(models.Model):
    fromUser = models.ForeignKey(Usuario, related_name='from_usr', on_delete=models.CASCADE)
    toUser = models.ForeignKey(Usuario, related_name='to_usr', on_delete=models.CASCADE)

class Premium(models.Model):
    UsuarioRegistrado = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                             related_name='Premium')

    def __str__(self):
        return self.UsuarioRegistrado.NombreUsuario


class NoPremium(models.Model):
    # WARNING: Es posible que falte la reestriccion de max y min
    UsuarioRegistrado = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                             related_name='NoPremium')
    NumSalt = models.IntegerField()

    def __str__(self):
        return self.UsuarioRegistrado.NombreUsuario


class CreadorContenido(models.Model):
    UsuarioRegistrado = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                             related_name='CreadorContenido')

    def __str__(self):
        return self.UsuarioRegistrado.NombreUsuario


class Audio(models.Model):
    ID = models.AutoField(primary_key=True)
    FicheroDeAudio = models.FileField(null=False, upload_to='audio')
    Titulo = models.CharField(max_length=30, null=False)
    Idioma = models.CharField(max_length=15, null=False)
    Duracion = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    CreadorDeContenido = models.ForeignKey(CreadorContenido, null=False, blank=False,
                                           on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ID', 'CreadorDeContenido')

    def __str__(self):
        return self.Titulo

    def getURL(self, httphost):
        return 'https://' + httphost + settings.MEDIA_URL + self.FicheroDeAudio.name


class Cancion(models.Model):
    AudioRegistrado = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE)
    UsuariosComoFavorita = models.ManyToManyField(Usuario, blank=True, related_name='Favoritas')

    def __str__(self):
        formato = 'Cancion {0} subida por {1}'
        return formato.format(self.AudioRegistrado.Titulo, self.AudioRegistrado.CreadorDeContenido)

    def getURL(self, httphost):
        return 'https://' + httphost + settings.MEDIA_URL + self.AudioRegistrado.FicheroDeAudio.name


class Artista(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30, unique=True)
    PaisDeNacimiento = models.CharField(max_length=30)
    Canciones = models.ManyToManyField(Cancion, blank=True, related_name='Artistas')

    def __str__(self):
        return self.Nombre


class Album(models.Model):
    ID = models.AutoField(primary_key=True)
    NombreAlbum = models.CharField(max_length=100, null=False)
    Canciones = models.ManyToManyField(Cancion, blank=False, related_name='Albunes')
    FotoDelAlbum = models.ImageField()
    Fecha = models.DateField(null=False)

    def __str__(self):
        return self.NombreAlbum

    def getFotoDelAlbum(self, httphost):
        return 'https://' + httphost + settings.MEDIA_URL + self.FotoDelAlbum.name


class Genero(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    # Por el momento se puden crear Geenros vacios
    Canciones = models.ManyToManyField(Cancion, blank=True, related_name='Generos')

    def __str__(self):
        return self.Nombre


class PlayList(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    Privado = models.BooleanField(null=False)
    UsuarioNombre = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Canciones = models.ManyToManyField(Cancion, blank=True, related_name='PlayLists')

    class Meta:
        unique_together = ('ID', 'UsuarioNombre')

    def __str__(self):
        formato = 'Playlist {0} del usuario {1}'
        return formato.format(self.Nombre, self.UsuarioNombre)


class Carpeta(models.Model):
    ID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    PlayList = models.ManyToManyField(PlayList, blank=True, related_name='Carpetas')

    def __str__(self):
        formato = 'Carpeta {0}'
        return formato.format(self.Nombre)


class Capitulo(models.Model):
    AudioRegistrado = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE)
    Fecha = models.DateField(null=False)

    def __str__(self):
        formato = 'Capitulo {0} subida por {1}'
        return formato.format(self.AudioRegistrado.Titulo, self.AudioRegistrado.CreadorDeContenido)

    def getURL(self, httphost):
        return 'https://' + httphost + settings.MEDIA_URL + self.AudioRegistrado.FicheroDeAudio.name


class Podcast(models.Model):
    Nombre = models.CharField(max_length=50, null=False)
    Descripcion = models.TextField(null=False)
    Subscriptores = models.ManyToManyField(Usuario, blank=True, related_name='Suscrito')
    Capitulos = models.ForeignKey(Capitulo, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre


class Interlocutor(models.Model):
    Nombre = models.CharField(max_length=50, null=False)
    Podcasts = models.ManyToManyField(Podcast, blank=True, related_name='Participan')

    def __str__(self):
        return self.Nombre


class AudioEscuchado(models.Model):
    ID = models.AutoField(primary_key=True)
    Usuario = models. ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Audio = models.ForeignKey(Audio, null=False, blank=False, on_delete=models.CASCADE)
    TimeStamp = models.TimeField(null=False)

    def __str__(self):
        formato = 'Audio {0} escuchado por {1} en el instante {2}'
        return formato.format(self.Audio.Titulo, self.Usuario.NombreUsuario, self.TimeStamp)

    class Meta:
        unique_together = ('Usuario', 'Audio', 'TimeStamp')
