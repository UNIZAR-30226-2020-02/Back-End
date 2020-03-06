from django.db import models


# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=25, primary_key=True)
    Contrasenya = models.CharField(max_length=50, null=False)
    Correo = models.CharField(max_length=100, null=False)
    FotoDePerfil = models.ImageField(null=False)
    Seguidos = models.ManyToManyField("self")


class Premium(models.Model):
    NombrePremium = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE, primary_key=True,
                                         parent_link=True)


class NoPremium(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE, primary_key=True,
                                  parent_link=True)
    NumSalt = models.IntegerField()

class CreadorContenido(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE, primary_key=True,
                                  parent_link=True)

class Genero(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=1000, null=False)

class Audio(models.Model):
    FicheroDeAudio = models.FileField(null=False)
    Titulo = models.CharField(max_length=30, null=False)
    Idioma = models.CharField(max_length=15, null=False)
    ID = models.IntegerField(primary_key=True)
    Duracion = models.DecimalField( max_digits=5, decimal_places=2, null=False)
    CreadorDeContenido = models.ForeignKey(CreadorContenido, null=False, blank=False,
                                           on_delete=models.CASCADE)

class Podcast(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE, primary_key=True,
                              parent_link=True)
    Resumen = models.CharField(max_length=1000, null=False)


class Cancion(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE, primary_key=True,
                              parent_link=True)


class PlayList(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    UsuarioNombre = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

class Carpeta(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)


class Artista(models.Model):
    Nombre = models.CharField(max_length=30, primary_key=True)
    PaisDeNacimiento = models.CharField(max_length=15)


class Almacenar(models.Model):
    CarpetaID = models.ForeignKey(Carpeta, null=False, blank=False, on_delete=models.CASCADE)
    PlayListID = models.ForeignKey(PlayList, null=False, blank=False, on_delete=models.CASCADE)


class Pertenece(models.Model):
    AudioID = models.ForeignKey(Audio, null=False, blank=False, on_delete=models.CASCADE)
    GeneroID = models.ForeignKey(Genero, null=False, blank=False, on_delete=models.CASCADE)

class SerFavorita(models.Model):
    AudioID = models.ForeignKey(Audio, null=False, blank=False, on_delete=models.CASCADE)
    UsuarioNombre = models.ForeignKey(Usuario, null=False, blank=False,
                                      on_delete=models.CASCADE)


class Componer(models.Model):
    ArtistaNombre = models.ForeignKey(Artista, null=False, blank=False,
                                      on_delete=models.CASCADE)
    Audio = models.ForeignKey(Audio, null=False, blank=False, on_delete=models.CASCADE)
