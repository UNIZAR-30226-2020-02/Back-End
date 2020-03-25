from rest_framework import serializers

from .models import *



class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = ['Nombre']