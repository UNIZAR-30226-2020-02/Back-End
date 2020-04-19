from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from django.http import JsonResponse
from django.conf import settings
from rest_framework.parsers import JSONParser
from django.db.models import Q
from .serializer import *
from .models import *
from .forms import *
import math
import os
import binascii
import datetime
import re
from .functions import *

# Permite la creacion de carpetas pasando los campos
# del cuerpo al serializer
@api_view(['POST'])
def CreateFolder(request):
    if request.method == "POST":
        serializer = CarpetaSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Permite la creacion de usuarios especificando su tipo
# pasando los campos del cuerpo al serializer
@api_view(['POST'])
@parser_classes([JSONParser])
def CreateUser(request):
    if request.method == "POST":

        request.data['Contrasenya'] = encrypt(str.encode(request.data['Contrasenya'])).hex()
        request.data['NombreUsuario'] = encrypt(str.encode(request.data['NombreUsuario'])).hex()
        request.data['Correo'] = encrypt(str.encode(request.data['Correo'])).hex()
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
def CreateUserImg(request):
    inform = [{'inform': ''}]

    if request.method == 'POST':
        request.data['Contrasenya'] = encrypt(str.encode(request.data['Contrasenya'])).hex()
        request.data['NombreUsuario'] = encrypt(str.encode(request.data['NombreUsuario'])).hex()
        request.data['Correo'] = encrypt(str.encode(request.data['Correo'])).hex()
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
        return JsonResponse(inform, safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)


# Permite la creacion de usuarios especificando su tipo
# pasando los campos del cuerpo al serializer
@api_view(['POST'])
@parser_classes([JSONParser])
def Login(request):
    inform = [{'inform': ''}]

    if request.method == "POST":

        try:

            hashname = encrypt(str.encode(request.data['NombreUsuario'])).hex()
            hashpassword = encrypt(str.encode(request.data['Contrasenya'])).hex()
            usuario = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))

        except Usuario.DoesNotExist:

            inform[0] = 'Usuario no registrado'
            return JsonResponse(inform, safe=False, status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            inform[0] = 'Los campos del request estan mal escirtos'
            JsonResponse(inform, safe=False, status=status.HTTP_400_BAD_REQUEST)

        if usuario.Contrasenya != hashpassword:
            inform[0] = 'Contraseña incorrecta'
            return JsonResponse(inform, safe=False, status=status.HTTP_401_UNAUTHORIZED)

        inform[0] = 'Usuario autenticado correctamente'
        return JsonResponse(inform, safe=False, status=status.HTTP_200_OK)

    else:

        inform[0] = 'Solo validas peticiones POST'
        JsonResponse(inform, safe=False, status=status.HTTP_406_NOT_ACCEPTABLE)


# Permite la actualizacion de
# la imegen de un usuario
@api_view(['POST'])
def UpdatePerfilImage(request):
    if request.method == "POST":

        try:

            hashname = encrypt(str.encode(request.data['NombreUsuario'])).hex()
            user = Usuario.objects.get(NombreUsuario=hashname)
            user.FotoDePerfil = request.FILES['NuevaFoto']
            user.save()
            # De este modo no se gurdan las imagens en /images
            # Usuario.objects.filter(NombreUsuario=request.data['NombreUsuario']).update(FotoDePerfil=request.FILES['NuevaFoto'])
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)
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

        data = [{'URL': audio.getURL(request.META['HTTP_HOST'])}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Recuoera una cancion de la
# de base de datos
@api_view(['GET'])
@parser_classes([JSONParser])
def GetSong(request):
    if request.method == "GET":

        try:

            cancion = Cancion.objects.get(AudioRegistrado__Titulo=request.query_params['Titulo'])

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        data = [{'URL': cancion.getURL(request.META['HTTP_HOST'])}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Recupera un podcast de la base
# de datos
@api_view(['GET'])
@parser_classes([JSONParser])
def GetPodcastChapter(request):
    if request.method == "GET":

        try:

            capitulo = Capitulo.objects.get(AudioRegistrado__Titulo=request.query_params['Titulo'])

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        data = [{'URL': capitulo.getURL(request.META['HTTP_HOST'])}]
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
@parser_classes([JSONParser])
def GivePermissions(request):
    if request:

        try:

            hashname = encrypt(str.encode(request.data['NombreUsuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))

            if request.data['Tipo'] == 'NoPremium':

                NoPremium(UsuarioRegistrado=user, NumSalt=10).save()
                return Response(status=status.HTTP_200_OK)

            elif request.data['Tipo'] == 'Premium':

                Premium(UsuarioRegistrado=user).save()
                return Response(status=status.HTTP_200_OK)

            elif request.data['Tipo'] == 'CreadorDeContenido':

                CreadorContenido(UsuarioRegistrado=user).save()
                return Response(status=status.HTTP_200_OK)

            else:

                return Response(status=status.HTTP_400_BAD_REQUEST)


        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
@parser_classes([JSONParser])
def UpdatePermissions(request):
    if request.method == "POST":

        try:

            hashname = encrypt(str.encode(request.data['NombreUsuario'])).hex()
            user = Usuario.objects.get(NombreUsuario=hashname)

            if NoPremium.objects.filter(UsuarioRegistrado=user).exists():

                if request.data['NuevoTipo'] == 'NoPremium':

                    return Response(status=status.HTTP_304_NOT_MODIFIED)

                else:

                    NoPremium.objects.filter(UsuarioRegistrado=user).delete()

            elif Premium.objects.filter(UsuarioRegistrado__NombreUsuario=hashname).exists():

                if request.data['NuevoTipo'] == 'Premium':
                    return Response(status=status.HTTP_304_NOT_MODIFIED)
                else:
                    Premium.objects.filter(UsuarioRegistrado=user).delete()

            elif CreadorContenido.objects.filter(UsuarioRegistrado__NombreUsuario=hashname).exists():

                if request.data['NuevoTipo'] == 'CreadorContenido':
                    return Response(status=status.HTTP_304_NOT_MODIFIED)
                else:
                    CreadorContenido.objects.filter(UsuarioRegistrado=user).delete()

            else:

                return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.data['NuevoTipo'] == 'CreadorContenido':

            CreadorContenido.objects.filter(UsuarioRegistrado=user).save()

        elif request.data['NuevoTipo'] == 'Premium':

            Premium.objects.filter(UsuarioRegistrado=user).save()

        elif request.data['NuevoTipo'] == 'NoPremium':

            NoPremium.objects.filter(UsuarioRegistrado=user).save()

        else:

            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
@parser_classes([JSONParser])
def GetUserInfo(request):
    data = {'NombreUsuario': '', 'Correo': ''}

    if request.method == "GET":

        try:

            hashname = encrypt(str.encode(request.query_params['NombreUsuario'])).hex()
            print(hashname)
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            data['NombreUsuario'] = decrypt(binascii.unhexlify(user.NombreUsuario)).decode('ascii')
            data['Correo'] = decrypt(binascii.unhexlify(user.Correo)).decode('ascii')
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(tatus=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Actualiza los campos del usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def UpdateUserFields(request):
    if request.method == "POST":

        try:

            hashname = encrypt(str.encode(request.data['NombreUsuarioActual'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            user.NombreUsuario = encrypt(str.encode(request.data['NuevoNombreUsuario'])).hex()
            user.save()
            # Podria hacerse con update(No probado)
            # Usuario.objects.filter(NombreUsuario=request.data['NombreUsuario']).update(FotoDePerfil=request.FILES['NuevaFoto'])
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except  KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Devuelve todos los usuarios existentes
# en la base de datos
@api_view(['GET'])
def GetAllUser(request):
    if request.method == "GET":
        # Obtencion de todos los objetos de tipo usuario
        users = Usuario.objects.all()
        # Creacion de un serializer para generar la respuesta
        serializer = UsuarioSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Devuelve todas las canciones almacenada
# en la base de datos
@api_view(['GET'])
def GetAllSongs(request):
    if request.method == "GET":

        listOfArtists = []
        listOfGenders = []
        listOfAlbuns = []
        listOfImages = []
        listOfSongs = []
        data = {}
        songs = Cancion.objects.all()

        for index in range(songs.count()):

            artistsOfSong = songs[index].Artistas.all()
            for index2 in range(artistsOfSong.count()):
                listOfArtists += [artistsOfSong[index2].Nombre]
            albunsOfSong = songs[index].Albunes.all()
            for index3 in range(albunsOfSong.count()):
                listOfAlbuns += [albunsOfSong[index3].NombreAlbum]
                listOfImages += [albunsOfSong[index3].getFotoDelAlbum(request.META['HTTP_HOST'])]

            gendersOfSong = songs[index].Generos.all()
            for index4 in range(gendersOfSong.count()):
                listOfGenders += [gendersOfSong[index4].Nombre]
            listOfSongs += [dict.fromkeys({'Artistas', 'url', 'Albumes', 'ImagenesAlbum','Generos'})]
            listOfSongs[index]['Artistas'] = listOfArtists
            listOfSongs[index]['url'] = songs[index].getURL(request.META['HTTP_HOST'])
            listOfSongs[index]['Albumes'] = listOfAlbuns
            listOfSongs[index]['ImagenesAlbums'] = listOfImages
            listOfSongs[index]['Generos'] = listOfGenders
            data[songs[index].AudioRegistrado.Titulo] = listOfSongs[index]
            listOfArtists = []
            listOfGenders = []
            listOfAlbuns = []
            listOfImages = []

        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


# Devuelve todas las canciones
# de un determinado genero
@api_view(['GET'])
@parser_classes([JSONParser])
def GetSongByGenre(request):
    if request.method == "GET":

        try:

            listaOfArtists = []
            listOfAlbuns = []
            listOfImages = []
            listOfSongs = []
            data = {}
            songs = Genero.objects.get(Nombre=request.query_params['NombreGenero']).Canciones.all()
            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            for index in range(songs.count()):

                artistsOfSong = songs[index].Artistas.all()
                for index2 in range(artistsOfSong.count()):
                    listaOfArtists += [artistsOfSong[index2].Nombre]
                    print(artistsOfSong[index2].Nombre)
                    print(listaOfArtists)
                albunsOfSong = songs[index].Albunes.all()
                for index3 in range(albunsOfSong.count()):
                    listOfAlbuns += [albunsOfSong[index3].NombreAlbum]
                    listOfImages += [albunsOfSong[index3].getFotoDelAlbum(request.META['HTTP_HOST'])]

                listOfSongs += [dict.fromkeys({'Artistas', 'url', 'Albumes', 'ImagenesAlbum','EsFavorita'})]
                listOfSongs[index]['Artistas'] = listaOfArtists
                listOfSongs[index]['url'] = songs[index].getURL(request.META['HTTP_HOST'])
                listOfSongs[index]['Albumes'] = listOfAlbuns
                listOfSongs[index]['ImagenesAlbum'] = listOfImages
                listOfSongs[index]['EsFavorita'] = songs[index].UsuariosComoFavorita.all().filter(NombreUsuario=hashname).exists()
                data[songs[index].AudioRegistrado.Titulo] = listOfSongs[index]
                listaOfArtists = []
                listOfAlbuns = []
                listOfImages = []

            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        except Genero.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Añade una nueva solicitud de amistad
# de un usuario a su lista
@api_view(['POST'])
@parser_classes([JSONParser])
def AddRequest(request):
    if request.method == "POST":

        try:

            hashfollower = encrypt(str.encode(request.data['NuevoSeguidor'])).hex()
            hashususer = encrypt(str.encode(request.data['Usuario'])).hex()
            seguidor = Usuario.objects.get(NombreUsuario=hashfollower)
            Usuario.objects.get(NombreUsuario=hashususer).SolicitudAmistad.add(seguidor)
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Devuelve la foto de perfil del usuario
@api_view(['GET'])
@parser_classes([JSONParser])
def GetProfilePhoto(request):
    if request.method == "GET":
        try:

            data = {'FotoDePerfil': ''}
            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            data['FotoDePerfil'] = user.getFotoDePerfil(request.META['HTTP_HOST'])
            print(data['FotoDePerfil'])
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Devuelve la ultimacancion escuchada
# por el usuario
@api_view(['GET'])
def GetLastSong(request):

    if request.method == "GET":

        listOfArtists = []
        listOfGenders = []
        listOfAlbuns = []
        listOfImages = []
        songData = {'Artistas': '', 'url': '', 'Albumes': '', 'ImagenesAlbums': '', 'Generos': ''}
        data = {}
        # Por el momento siempre es la misma
        song = Cancion.objects.get(AudioRegistrado__Titulo='Audio1')

        artistsOfSong = song.Artistas.all()
        for index2 in range(artistsOfSong.count()):
            listOfArtists += [artistsOfSong[index2].Nombre]
        albunsOfSong = song.Albunes.all()
        for index3 in range(albunsOfSong.count()):
            listOfAlbuns += [albunsOfSong[index3].NombreAlbum]
            listOfImages += [albunsOfSong[index3].getFotoDelAlbum(request.META['HTTP_HOST'])]

        gendersOfSong = song.Generos.all()
        for index4 in range(gendersOfSong.count()):
            listOfGenders += [gendersOfSong[index4].Nombre]

        songData['Artistas'] = listOfArtists
        songData['url'] = song.getURL(request.META['HTTP_HOST'])
        songData['Albumes'] = listOfAlbuns
        songData['ImagenesAlbums'] = listOfImages
        songData['Generos'] = listOfGenders
        data[song.AudioRegistrado.Titulo] = songData
        return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Permite que un susario
# siga a otro
@api_view(['GET'])
def Follow(request):

    if request.method == "GET":

        try:
            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            hashfollower = encrypt(str.encode(request.query_params['Seguidor'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            follower = Usuario.objects.get(Q(NombreUsuario=hashfollower) | Q(Correo=hashfollower))
            user.follow(follower)
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Devulve los seguidores
# de un usuario
@api_view(['GET'])
def GetFollowers(request):

    if request.method == "GET":

        try:
            data = {}
            listOfPhotos = []
            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            followers = user.getFollowers()
            for index in range(followers.count()):
                listOfPhotos += [dict.fromkeys({'FotoDePerfil'})]
                listOfPhotos[index]['FotoDePerfil'] = followers[index].getFotoDePerfil(request.META['HTTP_HOST'])
                decodename = decrypt(binascii.unhexlify(followers[index].NombreUsuario)).decode('ascii')
                data[decodename] = listOfPhotos[index]
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Devuelve los usarios
# a los que sigue un usuario
@api_view(['GET'])
def GetFollowing(request):

    if request.method == "GET":

        try:
            data = {}
            listOfPhotos = []

            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            following = user.getFollowing()
            for index in range(following.count()):
                listOfPhotos += [dict.fromkeys({'FotoDePerfil'})]
                listOfPhotos[index]['FotoDePerfil'] = following[index].getFotoDePerfil(request.META['HTTP_HOST'])
                decodename = decrypt(binascii.unhexlify(following[index].NombreUsuario)).decode('ascii')
                data[decodename] =  listOfPhotos[index]
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Añade una cancion a favoritos
# de un usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def AddSongToFavorites(request):

    if request.method == "POST":

        try:
            hashname = encrypt(str.encode(request.data['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            Cancion.objects.get(AudioRegistrado__Titulo=request.data['Titulo']).UsuariosComoFavorita.add(user)
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Audio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Elimina una cancion como
# favorita de un usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def RemoveSongFromFavorites(request):
    if request.method == "POST":
        try:

            hashname = encrypt(str.encode(request.data['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            song = Cancion.objects.get(AudioRegistrado__Titulo=request.data['Titulo'])
            song.UsuariosComoFavorita.remove(user)
            return Response(status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except Cancion.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Marca una canción como escuchada
# para un determinado usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def AddSongToListened(request):

    if request.method == "POST":

        try:

            hashname = encrypt(str.encode(request.data['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            audio = Audio.objects.get(Titulo=request.data['Titulo'])
            AudioEscuchado(Usuario=user, Audio=audio, TimeStamp=datetime.datetime.now().time()).save()
            return Response(status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        except Audio.DoesNotExist:

            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Dada una palbra clave
# retorna un conjunto de
# usuario
@api_view(['GET'])
def SearchUser (request):

    if request.method == "GET":
        try:
            data = {'Usuarios': ''}
            listOfUsers = []
            allUsers = Usuario.objects.all()
            keyWord = re.compile(request.query_params['KeyWord'])
            for index in range(allUsers.count()):

                decodename = decrypt(binascii.unhexlify(allUsers[index].NombreUsuario)).decode('ascii')
                if re.match(keyWord, decodename):
                    listOfUsers += [decodename]
            data['Usuarios'] = listOfUsers
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)




# Devulve las canciones
# favoritas de un usuario
@api_view(['GET'])
def GetFavoriteSongs(request):

    if request.method == "GET":

        listOfSongs = []
        listOfAlbuns = []
        listOfImages = []
        listOfArtists = []
        listOfGenders = []
        data = {}
        try:

            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            favoritesongs = user.Favoritas.all()
            for index in (range(favoritesongs.count())):
                artistsOfSong = favoritesongs[index].Artistas.all()
                for index2 in range(artistsOfSong.count()):
                    listOfArtists += [artistsOfSong[index2].Nombre]

                albunsOfSong = favoritesongs[index].Albunes.all()
                for index3 in range(albunsOfSong.count()):
                    listOfAlbuns += [albunsOfSong[index3].NombreAlbum]
                    listOfImages += [albunsOfSong[index3].getFotoDelAlbum(request.META['HTTP_HOST'])]

                gendersOfSong = favoritesongs[index].Generos.all()
                for index4 in range(gendersOfSong.count()):
                    listOfGenders += [gendersOfSong[index4].Nombre]

                listOfSongs += [dict.fromkeys({'Artistas', 'url', 'Albumes', 'ImagenesAlbums', 'Generos'})]
                listOfSongs[index]['Artistas'] = listOfArtists
                listOfSongs[index]['url'] = favoritesongs[index].getURL(request.META['HTTP_HOST'])
                listOfSongs[index]['Albumes'] = listOfAlbuns
                listOfSongs[index]['ImagenesAlbums'] = listOfImages
                listOfSongs[index]['Generos'] = listOfGenders
                data[favoritesongs[index].AudioRegistrado.Titulo] = listOfSongs[index]
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        except KeyError:

            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Crea una nueva playList
# Para un determinado usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def CreatePlayList(request):

    if request.method == "POST":
        try:
            hashname = encrypt(str.encode(request.query_params['Usuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))
            PlayList(Nombre=request.data['NombrePlayList'], Privado=request.data['EsPrivado'],UsuarioNombre=user).save()
            return Response(status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Añade una cancion a una
# play list de un determinado
# usuario
@api_view(['POST'])
@parser_classes([JSONParser])
def AddSongToPlayList(request):

    if request.method == "POST":

        try:
            hashname = encrypt(str.encode(request.data['Usuario'])).hex()
            song = Cancion.objects.get(AudioRegistrado__Titulo=request.data['Titulo'])
            PlayList.objects.get(UsuarioNombre__NombreUsuario=hashname).Canciones.add(song)
            return Response(status=status.HTTP_200_OK)

        except Cancion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# Devuelve las playlist de un usuario,
# y si es posible las fotos de 4 canciones
@api_view(['GET'])
#@parser_classes([JSONParser])
def GetUserPlaylists (request):
    print(request.query_params['NombreUsuario'])
    data = {'PlayLists': []}
    dataAux=[]
    playlist= {'NombrePlayList': '', 'Fotos':[]}
    if request.method == "GET":
        try:
            hashname = encrypt(str.encode(request.query_params['NombreUsuario'])).hex()
            user = Usuario.objects.get(Q(NombreUsuario=hashname) | Q(Correo=hashname))

            for p in PlayList.objects.filter(UsuarioNombre=user):
                playlist['NombrePlayList'] = p.Nombre

                fotos = []
                i=0
                for c in p.Canciones.order_by('id')[:4]:
                    album=Album.objects.get(Canciones=c)
                    fotos.append(album.getFotoDelAlbum(request.META['HTTP_HOST']))
                    i=i+1
                if i>0:
                    playlist['Fotos'] = fotos
                dataAux.append(playlist)
            data['PlayList']= dataAux
            return JsonResponse(data, safe=False, status=status.HTTP_200_OK)

        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
