from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from django.http import JsonResponse
from django.conf import settings
from rest_framework.parsers import JSONParser
from django.db.models import Q
import hashlib
from .serializer import *
from .models import *
from .forms import *

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
    else:

        return  Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Permite la creacion de usuarios especificando su tipo
# pasando los campos del cuerpo al serializer
@api_view(['POST'])
@parser_classes([JSONParser])
def CrearUsuario(request):

    if request.method == "POST":
        request.data['Contrasenya'] = hashlib.new("sha224", request.data['Contrasenya'].encode('utf-8')).hexdigest()
        request.data['NombreUsuario'] = hashlib.new("sha224", request.data['NombreUsuario'].encode('utf-8')).hexdigest()
        request.data['Correo'] = hashlib.new("sha224", request.data['Correo'].encode('utf-8')).hexdigest()
        nuevoUsuario = UsuarioSerializer(data=request.data)

        if nuevoUsuario.is_valid():

            nuevoUsuario.save()

            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Permite la creacion de usuarios con una imagen
# de perfil
@api_view(['POST'])
def CrearUsuarioConImg(request):

    inform = [{'inform': ''}]

    if request.method == 'POST':
        request.data['Contrasenya'] = hashlib.new("sha224", request.data['Contrasenya'].encode('utf-8')).hexdigest()
        request.data['NombreUsuario'] = hashlib.new("sha224", request.data['NombreUsuario'].encode('utf-8')).hexdigest()
        request.data['Correo'] = hashlib.new("sha224", request.data['Correo'].encode('utf-8')).hexdigest()
        form = UserForm(request.data, request.FILES)
        if form.is_valid():
            form.save()
            inform[0] = 'Creado correctamente'
            return JsonResponse(inform, safe=False, status=status.HTTP_200_OK)
        else:
            inform[0] = 'Campos invalidos'
            return JsonResponse(inform, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        inform[0] = 'La peticion debe ser POST'
        return JsonResponse(inform, safe=False, status= status.HTTP_406_NOT_ACCEPTABLE)


# Permite la creacion de usuarios especificando su tipo
# pasando los campos del cuerpo al serializer
@api_view(['POST'])
@parser_classes([JSONParser])
def Login(request):

    inform = [{'inform': ''}]

    if request.method == "POST":

        try:

            hashname = hashlib.new("sha224", request.data['NombreUsuario'].encode('utf-8')).hexdigest()
            hashpassword = hashlib.new("sha224", request.data['Contrasenya'].encode('utf-8')).hexdigest()
            usuario = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))

        except Usuario.DoesNotExist:

            inform[0] = 'Usuario no registrado'
            return JsonResponse(inform, safe=False,status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            inform[0] = 'Los campos del request estan mal escirtos'
            JsonResponse(inform, safe=False, status=status.HTTP_400_BAD_REQUEST)

        if usuario.Contrasenya != hashpassword:
            inform[0] = 'Contraseña incorrecta'
            return JsonResponse(inform, safe=False, status=status.HTTP_401_UNAUTHORIZED)

        inform[0] = 'Usuario autenticado correctamente'
        return JsonResponse(inform, safe=False,status=status.HTTP_200_OK)

    else:

        inform[0] = 'Solo validas peticiones POST'
        JsonResponse(inform, safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)

# Permite la actualizacion de
# la imegen de un usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def UpdatePerfilImage(request):

    if request.method == "POST":

        try:

            hashname = hashlib.new("sha224", request.data['NombreUsuario'].encode('utf-8')).hexdigest()
            user = Usuario.objects.get(NombreUsuario=hashname)
            user.FotoDePerfil = request.FILES['NuevaFoto']
            user.save()
            # De este modo no se gurdan las imagens en /images
            #Usuario.objects.filter(NombreUsuario=request.data['NombreUsuario']).update(FotoDePerfil=request.FILES['NuevaFoto'])
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Retorna la URL de la cancion solicitada cuyo titulo
# se especifica en el
@api_view(['GET'])
@parser_classes([JSONParser])
def GetAudio(request):

    if request.method == "GET":

        try:
            audio = Audio.objects.get(Titulo=request.query_params['Titulo'])

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        url = 'https://' + request.META['HTTP_HOST'] + settings.MEDIA_URL + audio.FicheroDeAudio.name
        data = [{'URL': url}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
@parser_classes([JSONParser])
def GetSong(request):

    if request.method == "GET":

        try:

            cancion = Cancion.objects.get(AudioRegistrado__Titulo=request.query_params['Titulo'])

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        url = 'https://' + request.META['HTTP_HOST'] + settings.MEDIA_URL + cancion.AudioRegistrado.FicheroDeAudio.name
        data = [{'URL': url}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
@parser_classes([JSONParser])
def GetCapituloPodcast(request):

    if request.method == "GET":

        try:

            capitulo = Capitulo.objects.get(AudioRegistrado__Titulo=request.query_params['Titulo'])

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        url = 'https://' + request.META['HTTP_HOST'] + settings.MEDIA_URL + capitulo.AudioRegistrado.FicheroDeAudio.name
        data = [{'URL': url}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


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
