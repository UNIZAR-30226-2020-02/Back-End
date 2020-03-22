from django.db import models


# Create your models here.

class Usuario(models.Model):
    NombreUsuario = models.CharField(max_length=25, null=False, unique=True)
    Contrasenya = models.CharField(max_length=50, null=False)
    Correo = models.CharField(max_length=100, null=False, unique=True)
    FotoDePerfil = models.ImageField()
    Seguidos = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.NombreUsuario


class Premium(models.Model):
    NombrePremium = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                         parent_link=True)

    def __str__(self):
        return self.NombrePremium


class NoPremium(models.Model):
    Nombre = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                  parent_link=True)  # WARNING: Es posible que falte la reestriccion de max y min
    NumSalt = models.IntegerField()

    def __str__(self):
        return self.Nombre


class CreadorContenido(models.Model):
    NombreCreador = models.OneToOneField(Usuario, null=False, blank=False, on_delete=models.CASCADE,
                                         parent_link=True)

    def __str__(self):
        return self.NombreCreador


class Audio(models.Model):
    ID = models.IntegerField(primary_key=True)
    FicheroAudio = models.FileField(null=False)
    Titulo = models.CharField(max_length=30, null=False)
    Idioma = models.CharField(max_length=15, null=False)
    Duracion = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    CreadorDeContenido = models.ForeignKey(CreadorContenido, null=False, blank=False,
                                           on_delete=models.CASCADE)
    UsuariosComoFavorita = models.ManyToManyField(Usuario, blank=True, related_name='Audios')

    class Meta:
        unique_together = ('ID', 'CreadorDeContenido')

    def __str__(self):
        return self.Titulo


class Cancion(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE,
                              parent_link=True)

    def __str__(self):
        return self.ID


class Artista(models.Model):
    Nombre = models.CharField(max_length=30, unique=True)
    PaisDeNacimiento = models.CharField(max_length=30)
    Canciones = models.ManyToManyField(Audio, blank=True, related_name='Artistas')

    def __str__(self):
        return self.Nombre


class Album(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Canciones = models.ManyToManyField(Audio, blank=False, related_name='Albunes')

    def __str__(self):
        return self.Nombre


class Genero(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100, null=False)
    Canciones = models.ManyToManyField(Audio, blank=True, related_name='Generos')

    def __str__(self):
        return self.Nombre


class PlayList(models.Model):
    ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    Privado = models.BooleanField(null=False)
    UsuarioNombre = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ID', 'UsuarioNombre')

    def __str__(self):
        return self.Nombre


class Carpeta(models.Model):
    # ID = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=False)
    PlayList = models.ManyToManyField(PlayList, blank=True, related_name='Carpetas')

    def __str__(self):
        return self.Nombre


class Capitulo(models.Model):
    ID = models.OneToOneField(Audio, null=False, blank=False, on_delete=models.CASCADE,
                              parent_link=True)

    def __str__(self):
        return self.ID


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
