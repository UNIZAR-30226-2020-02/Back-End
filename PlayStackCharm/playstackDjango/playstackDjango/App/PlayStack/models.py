from django.db import models


# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=25, primary_key=True)
    Contrasenya = models.CharField(max_length=50,null=False)
    Correo = models.CharField(max_length=100,null=False)
    FotoDePerfil = models.ImageField(null=False)


class Premium(models.Model):
    Nombre = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class NoPremium(models.Model):
    Nombre = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    NumSalt = models.IntegerField(max_length=2)


class CreadorContenido(models.Model):
    Nombre = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class Genero(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=1000,null=Fasle)


class Audio(models.Model):
    FicheroDeAudio = models.FileField();
    Titulo = models.CharField(max_length=30, null=False)
    Idioma = models.CharField(max_length=15, null=False)
    ID = models.IntegerField(primary_key=True)
    Duracion = models.DecimalField( null=False)
    CreadorDeContenido = models.ForeignKey(CreadorContenido.Nombre, null=False, blank=False, on_delete=models.CASCADE,primary_key=True)


class Podcast(models.Model):
    ID = models.ForeignKey(Audio.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    Resumen = models.CharField(max_length=1000, null=False)


class Cancion(models.Model):
    ID = models.ForeignKey(Audio.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class PlayList(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(null=False)
    UsuarioNombre = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class Carpeta(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)


class Artista(models.Model):
    Nombre = models.CharField(max_length=30, primary_key=True)
    PaisDeNacimiento = models.CharField(max_length=15)


class Alamcenar(models.Model):
    CarpetaID = models.IntegerField(primary_key=True)
    PlayListID = models.ForeignKey(PlayList.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    PlayListUsuarioNombre = models.ForeignKey(PlayList.UsuarioNombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class Contiene(models.Model):
    AudioID = models.ForeignKey(Audio.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    AudioCreadorContenidoNombre = models.ForeignKey(Audio.CreadorDeContenido, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    PlayListID = models.ForeignKey(PlayList.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    PlayListUsuarioNombre = models.ForeignKey(PlayList.UsuarioNombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class Pertenece(models.Model):
    AudioID = models.ForeignKey(Audio.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    AudioCreadorContenidoNombre = models.ForeignKey(Audio.CreadorDeContenido, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    GeneroID = models.ForeignKey(Genero.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class Seguir(models.Model):
    UsuarioNombre1 = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    UsuarioNombre2 = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)


class SerFavorita(models.Model):
    AudioID = models.ForeignKey(Audio.ID, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    AudioCreadorContenidoNombre = models.ForeignKey(Audio.CreadorDeContenido, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    UsuarioNombre = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)

class Componer(models.Model):
    ArtistaNombre = models.ForeignKey(Artista.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    AudioCreadorDeContendio = models.ForeignKey(Audio.CreadorDeContenido, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)
    UsuarioNombre = models.ForeignKey(Usuario.Nombre, null=False, blank=False, on_delete=models.CASCADE, primary_key=True)

