from django.db import models


# Create your models here.


class Usuario(models.Model):
    Nombre = models.CharField(max_length=25, primary_key=True)
    Contrasenya = models.CharField(max_length=50, null=False)
    Correo = models.CharField(max_length=100)
    FotoDePerfil = models.ImageField(null=False)
    Seguidos = models.ManyToManyField('self')


class Premium(models.Model):
    NombrePremium = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                         parent_link=True)


class NoPremium(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                  parent_link=True)
    NumSalt = models.IntegerField()


class CreadorContenido(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                  parent_link=True)


class Audio(models.Model):
    IDAudio = models.IntegerField(primary_key=True)
    FicheroDeAudio = models.FileField(null=False)
    Titulo = models.CharField(max_length=30, null=False)
    Idioma = models.CharField(max_length=15, null=False)
    Duracion = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    CreadorDeContenido = models.ForeignKey(CreadorContenido, null=False, blank=False,
                                           on_delete=models.CASCADE)
    UsuariosComoFavorita = models.ManyToManyField(Usuario, blank=False)

    class Meta:
        unique_together = ('IDAudio', 'CreadorDeContenido')


class Artista(models.Model):
    Nombre = models.CharField(max_length=30, primary_key=True)
    PaisDeNacimiento = models.CharField(max_length=15)
    Canciones = models.ManyToManyField(Audio, blank=False)


class Genero(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=1000, null=False)
    Canciones = models.ManyToManyField(Audio, blank=False)


class Podcast(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE,
                              parent_link=True)
    Resumen = models.CharField(max_length=1000, null=False)


class Cancion(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE,
                              parent_link=True)


class PlayList(models.Model):
    IDPlayList = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    UsuarioNombre = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('IDPlayList', 'UsuarioNombre')


class Carpeta(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    PlayList = models.ManyToManyField(PlayList, blank=False)
