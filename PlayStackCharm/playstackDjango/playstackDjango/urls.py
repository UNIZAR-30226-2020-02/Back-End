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
    url('search/', views.Search, name='Search'), # *
    url('create/folder', views.CreateFolder, name='CreateFolder'),  # *
    url('create/album', views.CreateAlbum, name='CreateAlbum'), # *
    url('create/podcastchapter', views.CreateCapituloPodcast, name='CreateCapituloPodcast'), # *
    url('create/podcast', views.CreatePodcast, name='CreatePodcast'), # *
    url('create/song', views.CreateSong, name='CreateSong'),
    url('create/user', views.CreateUser, name='CreateUser'),    # *
    url('create/user/withimg', views.CreateUserImg, name='CreateUserImg'), # * Falta poner fichero
    url('create/playlist', views.CreatePlayList, name='CreatePlayList'),
    url('audio/remove', views.RemoveAudio, name='RemoveAudio'),
    url('song/update', views.SongUpdate, name='SongUpdate'),
    url('chapter/update', views.ChapterUpdate, name='ChapterUpdate'),
    url('get/allusers', views.GetAllUser, name='GetAllUser'), # *
    url('get/allsongs', views.GetAllSongs, name='GetAllSongs'), # ^
    url('get/allartists', views.GetAllArtists, name='GetAllArtists'),  # *
    url('get/allgenders', views.GetAllGenders, name='GetAllGenders'),
    url('get/allpodcasts', views.GetAllPodcasts, name='GetAllPodcasts'),
    url('get/podcast/all', views.GetPodcastCaps, name='GetPodcastCaps'),
    url('get/podcast/bytema', views.GetPodcastByTema, name='GetPodcastByTema'),
    url('get/podcast/byinterlocutor', views.GetPodcastByInterlocutor, name='GetPodcastByInterlocutor'),
    url('get/podcast/followed', views.GetSubscribedPodcast, name='GetSubscribedPodcast'),
    url('get/randomalbums', views.GetRandomAlbums, name='GetRandomAlbums'),  # *
    url('get/song/bygenre', views.GetSongByGenre, name='GetSongByGenre'), # *
    url('get/song/byartist', views.GetSongByArtist, name='GetSongByArtist'),  # *
    url('get/song/byalbum', views.GetSongByAlbum, name='GetSongByAlbum'),  # *
    url('get/artist/albums', views.GetArtistAlbums, name='GetArtistAlbums'),  # *
    #url('get/artist/singles', views.GetArtistAlbums, name='GetArtistAlbums'),  # *
    url('get/audio', views.GetAudio, name='GetAudio'), # *
    url('get/song', views.GetSong, name='GetSong'), # *
    url('get/chapter', views.GetPodcastChapter, name='GetPodcastChapter'), # *
    url('get/folders', views.GetUserFolders, name='GetUserFolders'),  # *
    url('get/playlists', views.GetUserPlaylists, name='GetUserPlaylists'),  # *
    url('get/playlist/songs', views.GetPlaylistSongs, name='GetPlaylistSongs'),  # *
    url('get/publicplaylists', views.GetUserPublicPlaylists, name='GetUserPublicPlaylists'),  # *
    url('get/favoritesongs', views.GetFavoriteSongs, name='GetFavoriteSongs'),  # *
    url('user/login', views.Login, name='Login'),  # *
    url('user/get/info', views.GetUserInfo, name='GetUserInfo'),  # *
    url('user/get/permissions', views.GetPermissions, name='GetPermissions'),
    url('user/get/lastsongs', views.GetLastSongs, name='GetLastSongs'),
    url('user/get/lastsong', views.GetLastSong, name='GetLastSong'),
    url('user/get/profilephoto', views.GetProfilePhoto, name='GetProfilePhoto'),
    url('user/get/followrequests', views.GetFollowRequests, name='GetFollowRequests'),
    url('user/get/following', views.GetFollowing, name='GetFollowing'),
    url('user/get/followers', views.GetFollowers, name='GetFollowers'),
    url('user/get/mostListenedSongs', views.GetMostListenedSongs, name='GetMostListenedSongs'),
    url('user/givepermissions', views.GivePermissions, name='GivePermissions'),  # *
    url('user/update/playlist', views.updatePlaylist, name='updatePlaylist'),
    url('user/update/folder', views.updateFolder, name='updateFolder'),
    url('user/update/image', views.UpdatePerfilImage, name='UpdatePerfilImage'), # *
    url('user/update/permissions', views.UpdatePermissions, name='UpdatePermissions'), # *
    url('user/update/fields', views.UpdateUserFields, name='UpdateUserFields'),  # ^
    url('user/add/request', views.AddRequest, name='AddRequest'),
    url('user/add/song/tofavorites', views.AddSongToFavorites, name='AddSongToFavorites'),
    url('user/add/song/tolistened', views.AddSongToListened, name='AddSongToListened'),
    url('user/add/song/toplaylist', views.AddSongToPlayList, name='AddSongToPlayList'),
    url('user/add/playlist/tofolder', views.addPlayListToFolder, name='addPlayListToFolder'),
    url('user/add/followRequest', views.AddUserFollowResquest, name='AddUserFollowResquest'), #Enviar solicitud de follow
    url('user/remove/followRequest', views.RemoveUserFollowResquest, name='RemoveUserFollowResquest'),
    url('user/reject/followRequest', views.RejectFollowResquest, name='RejectFollowResquest'),
    url('user/remove/follower', views.AddUserFollowResquest, name='RemoveFollower'),
    url('user/remove/song/fromfavorites', views.RemoveSongFromFavorites, name='RemoveSongFromFavorites'),
    url('user/remove/song/fromplaylist', views.removePlaylistSong, name='removePlaylistSong'),
    url('user/remove/playlist/fromfolder', views.removePlayListFromFolder, name='removePlayListFromFolder'),
    url('user/remove/playlist/', views.removePlaylist, name='removePlaylist'),
    url('user/remove/folder/', views.removeFolder, name='removeFolder'),
    url('user/search', views.SearchUser, name='SearchUser'),
    url('user/socialsearch', views.SearchUserSocial, name='SearchUserSocial'),
    url('user/follow/podcast', views.FollowPodcast, name='FollowPodcast'),
    url('user/follow', views.Follow, name='Follow'),     #Aceptar solicitud de follow
    url('user/unfollow/podcast', views.UnfollowPodcast, name='UnfollowPodcast'),
    url('user/unfollow', views.Unfollow, name='Unfollow'),
    url('user/askforpremium', views.AskForPremium, name='AskForPremium')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
