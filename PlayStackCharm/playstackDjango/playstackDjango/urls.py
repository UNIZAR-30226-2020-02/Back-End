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
    url('admin/', admin.site.urls),
    # Ruta dentro del servidor para acceder al recurso UsuarioResource
    url('usuarios/', include(user_resource.urls)),
    url('create/folder', views.CrearCarpeta, name='CrearCarpeta'),
    url('create/user', views.CrearUsuario, name='CrearUsuario'),
    url('create/user/withimg', views.CrearUsuarioConImg, name='CrearUsuarioConImg'),
    url('get/allusers', views.getAllUser, name='GetAllUser'),
    url('get/song/bygenre', views.GetSongByGenre, name='GetSongByGenre'),
    url('get/audio', views.GetAudio, name='GetAudio'),
    url('get/song', views.GetSong, name='GetSong'),
    url('get/chapter', views.GetPodcastChapter, name='GetPodcastChapter'),
    url('user/login', views.Login, name='Login'),
    url('user/getinfo', views.GetUserInfo, name='GetUserInfo'),
    url('user/givepermissions', views.GivePermissions, name='GivePermissions'),
    url('user/update/image', views.UpdatePerfilImage, name='UpdatePerfilImage'),
    url('user/update/permissions', views.UpdatePermissions, name='UpdatePermissions'),
    url('user/update/fields', views.UpdateUserFields, name='UpdateUserFields')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
