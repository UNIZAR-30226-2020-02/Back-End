from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from django.http import JsonResponse
from django.conf import settings
from rest_framework.parsers import JSONParser
import hashlib
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
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

# Permite la creacion de usuarios especificando su tipo
# pasando los campos del cuerpo al serializer
@api_view(['POST'])
@parser_classes([JSONParser])
def CrearUsuario(request):

    if request.method == "POST":
        nuevoUsuario = UsuarioSerializer(data=request.data)

        if nuevoUsuario.is_valid():


            nuevoUsuario.save()

            """
            Cifrado de nombre de usuario y contraseña(No probado)
            nuevoUsuario.Contrasenya = hashlib.new("sha224", nuevoUsuario.Contrasenya).hexdigest()
            nuevoUsuario.NombreUsuario = hashlib.new("sha224",nuevoUsuario.NombreUsuario).hexdigest()
            """

            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Permite la creacion de usuarios especificando su tipo
# pasando los campos del cuerpo al serializer
@api_view(['POST'])
@parser_classes([JSONParser])
def Login(request):

    iform = [{'inform': ''}]

    if request.method == "POST":

        try:
            usuario = Usuario.objects.get(NombreUsuario=request.data['NombreUsuario'])

        except Usuario.DoesNotExist:

            iform[0] = 'Usuario no registrado'
            return JsonResponse(iform, safe=False,status=status.HTTP_404_NOT_FOUND)

        if usuario.Contrasenya != request.data['Contrasenya']:
            iform[0] = 'Contraseña incorrecta'
            return JsonResponse(iform, safe=False, status=status.HTTP_401_UNAUTHORIZED)

        iform[0] = 'Usuario autenticado correctamente'
        return JsonResponse(iform, safe=False,status=status.HTTP_200_OK)

    else:

        iform[0] = 'Solo validas peticiones POST'
        JsonResponse(iform, safe=False, status=status.HTTP_400_BAD_REQUEST)

# Retorna la URL de la cancion solicitada cuyo titulo
# se especifica en el
@api_view(['GET'])
@parser_classes([JSONParser])
def GetSong(request):

    if request.method == "GET":

        try:
            audio = Audio.objects.get(Titulo=request.query_params['Titulo'])

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        url = 'https://' + request.META['HTTP_HOST'] + settings.MEDIA_URL + audio.FicheroDeAudio.name
        data = [{'URL': url}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_400_BAD_REQUEST)


# Devuelve todos los usuarios existentes en la base de datos
@api_view(['GET'])
def getAllUser(request):

    if request.method == "GET":
        # Obtencion de todos los objetos de tipo usuario
        users = Usuario.objects.all()
        # Creacion de un serializer para generar la respuesta
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_400_BAD_REQUEST)
