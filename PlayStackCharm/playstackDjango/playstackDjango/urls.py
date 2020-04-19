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

    url('admin/', admin.site.urls),
    # Ruta dentro del servidor para acceder al recurso UsuarioResource
    url('usuarios/', include(user_resource.urls)),
    url('create/folder', views.CrearCarpeta, name='CrearCarpeta'),  # *
    url('create/user', views.CrearUsuario, name='CrearUsuario'),    # *
    url('create/user/withimg', views.CrearUsuarioConImg, name='CrearUsuarioConImg'), # * Falta poner fichero
    url('get/allusers', views.GetAllUser, name='GetAllUser'), # *
    url('get/allsongs', views.GetAllSongs, name='GetAllSongs'), # *
    url('get/song/bygenre', views.GetSongByGenre, name='GetSongByGenre'), # *
    url('get/audio', views.GetAudio, name='GetAudio'), # *
    url('get/song', views.GetSong, name='GetSong'), # *
    url('get/chapter', views.GetPodcastChapter, name='GetPodcastChapter'), # *
    url('user/login', views.Login, name='Login'),  # *
    url('user/get/info', views.GetUserInfo, name='GetUserInfo'),  # *
    url('user/get/lastsong', views.GetLastSong, name='GetLastSong'),
    url('user/get/profilephoto', views.GetProfilePhoto, name='GetProfilePhoto'),
    url('user/get/following', views.GetFollowing, name='GetFollowing'),
    url('user/get/favoritesongs', views.GetFavoriteSongs, name='GetFavoriteSongs'),
    url('user/get/followers', views.GetFollowers, name='GetFollowers'),
    url('user/givepermissions', views.GivePermissions, name='GivePermissions'),  # *
    url('user/update/image', views.UpdatePerfilImage, name='UpdatePerfilImage'), # *
    url('user/update/permissions', views.UpdatePermissions, name='UpdatePermissions'), # *
    url('user/update/fields', views.UpdateUserFields, name='UpdateUserFields'),  # ^
    url('user/add/request', views.AddRequest, name='AddRequest'),
    url('user/add/song/tofavorites', views.AddSongToFavorites, name='AddSongToFavorites'),
    url('user/add/song/tolistened', views.AddSongToListened, name='AddSongToListened'),
    url('user/search', views.SearchUser, name='SearchUser'),
    url('user/follow', views.Follow, name='Follow')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
