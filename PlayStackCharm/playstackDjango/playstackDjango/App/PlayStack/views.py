from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse

from .serializer import *
from .models import *
# Permite la creacion de carpetas pasando los campos
# del cuerpo al serializer
@api_view(['POST'])
def CrearCarpeta(request):

    if request.method == "POST":
        serializer = CarpetaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:

            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def CrearUsuario(request):

    if request.method == "POST":
        nuevoUsuario = UsuarioSerializer(data=request.data)

        if nuevoUsuario.is_valid():

            nuevoUsuario.save()
            return Response(nuevoUsuario.data, status=status.HTTP_200_OK)

        else:

            return Response(nuevoUsuario.data, status=status.HTTP_400_BAD_REQUEST)


# Devuelve todos los usuarios existentes en la base de datos
@api_view(['POST'])
def getAllUser(request):

    # Obtencion de todos los objetos de tipo usuario
    users = Usuario.objects.all()
    # Creacion de un serializer para generar la respuesta
    serializer = UsuarioSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

