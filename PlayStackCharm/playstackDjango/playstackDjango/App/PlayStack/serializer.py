from rest_framework import serializers

from .models import *

# Serializer que permite la creacion de usuarios
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['NombreUsuario', 'Contrasenya', 'Correo']

# Serializer que permite la creacion de carpetas
class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = ['Nombre']
