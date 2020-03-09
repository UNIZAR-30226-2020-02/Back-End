from django.db import models


# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=25, primary_key=True)
    Contrasenya = models.CharField(max_length=50, null=False)
    Correo = models.CharField(max_length=100)
    FotoDePerfil = models.ImageField()
    Seguidos = models.ManyToManyField('self')

    def __str__(self):
        return self.Nombre



class Premium(models.Model):
    NombrePremium = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                         parent_link=True)

    def __str__(self):
        return self.NombrePremium


class NoPremium(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                  parent_link=True)
    NumSalt = models.IntegerField()

    def __str__(self):
        return self.Nombre


class CreadorContenido(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                  parent_link=True)

    def __str__(self):
        return self.Nombre


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

    def __str__(self):
        return self.Titulo


class Artista(models.Model):
    Nombre = models.CharField(max_length=30, primary_key=True)
    PaisDeNacimiento = models.CharField(max_length=15)
    Canciones = models.ManyToManyField(Audio, blank=False, related_name='Artistas')

    def __str__(self):
        return  self.Nombre

class Genero(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=1000, null=False)
    Canciones = models.ManyToManyField(Audio, blank=False)

    def __str__(self):
        return self.Nombre


class Podcast(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE,
                              parent_link=True)
    Resumen = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return self.ID


class Cancion(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE,
                              parent_link=True)

    def __str__(self):
        return self.ID


class PlayList(models.Model):
    IDPlayList = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    UsuarioNombre = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('IDPlayList', 'UsuarioNombre')

    def __str__(self):
        return self.Nombre


class Carpeta(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    PlayList = models.ManyToManyField(PlayList, blank=False)

    def __str__(self):
        return self.Nombre

class Album(models.Model):
    ID = models.IntegerField(primary_key=True)
    NombreAlbum = models.CharField(max_length=1000, null=False)
    Canciones = models.ManyToManyField(Audio, blank=False)

    def __str__(self):
        return self.NombreAlbum