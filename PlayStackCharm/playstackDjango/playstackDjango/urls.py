"""playstackDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from playstackDjango.App.PlayStack.resources import *
from playstackDjango.App.PlayStack import views
from django.conf import settings
from django.conf.urls.static import static

user_resource = UsuarioResource()

urlpatterns = [

    # ¡¡¡ Se marcan con * las url ya documentadas en swaggerhub !!!
    # ¡¡¡ Se marcan con ^ las url pendientes de actualizar en swaggerhub !!!

    url(r'^admin/', admin.site.urls),
    # Ruta dentro del servidor para acceder al recurso UsuarioResource
    url(r'^usuarios/', include(user_resource.urls)),
    url(r'^create/folder', views.CreateFolder, name='CrearCarpeta'),  # *
    url(r'^create/playlist', views.CreatePlayList, name='CreatePlayList'),
    url(r'^create/user', views.CreateUser, name='CrearUsuario'),    # *
    url(r'^create/user/withimg', views.CreateUserImg, name='CrearUsuarioConImg'), # * Falta poner fichero
    url(r'^get/allusers', views.GetAllUser, name='GetAllUser'), # *
    url(r'^get/allsongs', views.GetAllSongs, name='GetAllSongs'), # *
    url(r'^get/song/bygenre', views.GetSongByGenre, name='GetSongByGenre'), # *
    url(r'^get/audio', views.GetAudio, name='GetAudio'), # *
    url(r'^get/song', views.GetSong, name='GetSong'), # *
    url(r'^get/chapter', views.GetPodcastChapter, name='GetPodcastChapter'), # *
    url(r'^user/login', views.Login, name='Login'),  # *
    url(r'^user/get/info', views.GetUserInfo, name='GetUserInfo'),  # *
    url(r'^user/get/lastsong', views.GetLastSong, name='GetLastSong'),
    url(r'^user/get/profilephoto', views.GetProfilePhoto, name='GetProfilePhoto'),
    url(r'^user/get/following', views.GetFollowing, name='GetFollowing'),
    url(r'^user/get/favoritesongs', views.GetFavoriteSongs, name='GetFavoriteSongs'),
    url(r'^user/get/followers', views.GetFollowers, name='GetFollowers'),
    url(r'^user/givepermissions', views.GivePermissions, name='GivePermissions'),  # *
    url(r'^user/update/image', views.UpdatePerfilImage, name='UpdatePerfilImage'), # *
    url(r'^user/update/permissions', views.UpdatePermissions, name='UpdatePermissions'), # *
    url(r'^user/update/fields', views.UpdateUserFields, name='UpdateUserFields'),  # ^
    url(r'^user/add/request', views.AddRequest, name='AddRequest'),
    url(r'^user/add/song/tofavorites', views.AddSongToFavorites, name='AddSongToFavorites'),
    url(r'^user/remove/song/fromfavorites', views.RemoveSongFromFavorites, name='RemoveSongFromFavorites'),
    url(r'^user/add/song/tolistened', views.AddSongToListened, name='AddSongToListened'),
    url(r'^user/add/song/playlist', views.AddSongToPlayList, name='AddSongToPlayList'),
    url(r'^user/search', views.SearchUser, name='SearchUser'),
    url(r'^user/follow', views.Follow, name='Follow'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
