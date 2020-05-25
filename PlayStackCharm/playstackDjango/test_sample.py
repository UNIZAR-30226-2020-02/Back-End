import requests
import json
'''
def test_CreateUser_clases_validas():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca'
    datos['Correo'] = 'fe@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, json=datos)
    assert request.status_code == 201

# Existe usuario
def test_CreateUser_clase_7():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca'
    datos['Correo'] = 'fe2@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, json=datos)
    assert request.status_code == 400

# Existe correo
def test_CreateUser_clase_8():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca2'
    datos['Correo'] = 'fe@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, json=datos)
    assert request.status_code == 400

# No existe campo NombreUsuario
def test_CreateUser_clase_9():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'Contrasenya' : '', 'Correo' : ''}

    datos['Correo'] = 'fe3@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, json=datos)
    assert request.status_code == 400

# No existe campo Contrasenya
def test_CreateUser_clase_10():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca3'
    datos['Correo'] = 'fe4@gamil.com'

    request = requests.post(url, json=datos)
    assert request.status_code == 400

# No existe campo Correo
def test_CreateUser_clase_11():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : ''}

    datos['NombreUsuario'] = 'federicoLorca4'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, json=datos)
    assert request.status_code == 400

# Se utiliza un metodo GET en lugar del POST
def test_CreateUser_clase_12():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca2'
    datos['Correo'] = 'fe2@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.get(url, json=datos)
    assert request.status_code == 405

def test_CreatePlayList_clases_validas():
    url = 'https://playstack.azurewebsites.net/create/playlist'
    datos = {'NombreUsuario': '', 'NombrePlayList': '', 'EsPrivado': ''}

    datos['NombreUsuario'] = 'Freeman'
    datos['NombrePlayList'] = 'PlayList_test'
    datos['EsPrivado'] = True
    request = requests.post(url, json=datos)
    assert request.status_code == 200

# Usuario no existe
def test_CreatePlayList_clase_5():
    url = 'https://playstack.azurewebsites.net/create/playlist'
    datos = {'NombreUsuario': '', 'NombrePlayList': '', 'EsPrivado': ''}

    datos['NombreUsuario'] = 'juanDeLaNuza'
    datos['NombrePlayList'] = 'PlayList_test_2'
    datos['EsPrivado'] = True
    request = requests.post(url, json=datos)
    assert request.status_code == 404

# No existe campo NombreUsuario
def test_CreatePlayList_clase_6():
    url = 'https://playstack.azurewebsites.net/create/playlist'
    datos = {'NombrePlayList': '', 'EsPrivado': ''}

    datos['NombrePlayList'] = 'PlayList_test_3'
    datos['EsPrivado'] = True
    request = requests.post(url, json=datos)
    assert request.status_code == 400

# No existe campo NombrePlayList
def test_CreatePlayList_clase_7():
    url = 'https://playstack.azurewebsites.net/create/playlist'
    datos = {'NombreUsuario': '', 'EsPrivado': ''}

    datos['NombreUsuario'] = 'Freeman'
    datos['EsPrivado'] = True
    request = requests.post(url, json=datos)
    assert request.status_code == 400

# No existe campo EsPrivado
def test_CreatePlayList_clase_8():
    url = 'https://playstack.azurewebsites.net/create/playlist'
    datos = {'NombreUsuario': '','NombrePlayList': ''}

    datos['NombreUsuario'] = 'Freeman'
    datos['NombrePlayList'] = 'PlayList_test_4'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

# Se utiliza un metodo GET en lugar del POST
def test_CreatePlayList_clase_9():
    url = 'https://playstack.azurewebsites.net/create/playlist'
    datos = {'NombreUsuario': '','NombrePlayList': '', 'EsPrivado': ''}

    datos['NombreUsuario'] = 'Freeman'
    datos['NombrePlayList'] = 'PlayList_test_4'
    datos['EsPrivado'] = True
    request = requests.get(url, json=datos)
    assert request.status_code == 405

def test_GetAllSongs_clases_validas():
    url = 'https://playstack.azurewebsites.net/get/allsongs?NombreUsuario=Freeman'
    request = requests.get(url)
    assert request.status_code == 200

# No existe el usuario
def test_GetAllSongs_clase_4():
    url = 'https://playstack.azurewebsites.net/get/allsongs?NombreUsuario=usuario_tester'
    request = requests.get(url)
    assert request.status_code == 404

# No existe el campo NombreUsuario
def test_GetAllSongs_clase_5():
    url = 'https://playstack.azurewebsites.net/get/allsongs'
    request = requests.get(url)
    assert request.status_code == 400

# Se utiliza un metodo POST en lugar del GET
def test_GetAllSongs_clase_6():
    url = 'https://playstack.azurewebsites.net/get/allsongs?NombreUsuario=usuario_tester'
    request = requests.post(url)
    assert request.status_code == 405

def test_GetSubscribedPodcast_clases_validas():
    url = 'https://playstack.azurewebsites.net/get/podcast/followed?NombreUsuario=Freeman'
    request = requests.get(url)
    assert request.status_code == 200

# Usuario no existe
def test_GetSubscribedPodcast_clase_4():
    url = 'https://playstack.azurewebsites.net/get/podcast/followed?NombreUsuario=usuario_test'
    request = requests.get(url)
    assert request.status_code == 404

# No existe el campo NombreUsuario
def test_GetSubscribedPodcast_clase_5():
    url = 'https://playstack.azurewebsites.net/get/podcast/followed'
    request = requests.get(url)
    assert request.status_code == 400

# Se utiliza un metodo POST en lugar del GET
def test_GetSubscribedPodcast_clase_6():
    url = 'https://playstack.azurewebsites.net/get/podcast/followed?NombreUsuario=Freeman'
    request = requests.post(url)
    assert request.status_code == 405

def test_GetSongByArtist_clases_validas():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreUsuario=Freeman&NombreArtista=Queen'
    request = requests.get(url)
    assert request.status_code == 200

# Usuario no existe
def test_GetSongByArtist_clase_6():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreUsuario=usuario_test&NombreArtista=Queen'
    request = requests.get(url)
    assert request.status_code == 404

# Artista no existe
def test_GetSongByArtist_clase_7():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreUsuario=Freeman&NombreArtista=artista_test'
    request = requests.get(url)
    assert request.status_code == 404

# No existe el campo NombreUsuario
def test_GetSongByArtist_clase_8():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreArtista=Queen'
    request = requests.get(url)
    assert request.status_code == 400

# No existe el campo NombreArtista
def test_GetSongByArtist_clase_9():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreUsuario=Freeman'
    request = requests.get(url)
    assert request.status_code == 400

# Se utiliza un metodo POST en lugar del GET
def test_GetSongByArtist_clase_10():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreUsuario=Freeman&NombreArtista=Queen'
    request = requests.post(url)
    assert request.status_code == 405

def test_GetSongByArtist_clases_validas():
    url = 'https://playstack.azurewebsites.net/get/song/byartist?NombreUsuario=Freeman&NombreArtista=Queen'
    request = requests.get(url)
    assert request.status_code == 200

def test_GetUserPlaylists_clases_validas():
    url = 'https://playstack.azurewebsites.net/get/playlists?NombreUsuario=Freeman'
    request = requests.get(url)
    assert request.status_code == 200

# No existe Usuario
def test_GetUserPlaylists_clase_4():
    url = 'https://playstack.azurewebsites.net/get/playlists?NombreUsuario=usuario_test'
    request = requests.get(url)
    assert request.status_code == 404

# No existe campo NombreUsuario
def test_GetUserPlaylists_clase_5():
    url = 'https://playstack.azurewebsites.net/get/playlists'
    request = requests.get(url)
    assert request.status_code == 400

# Se utiliza un metodo POST en lugar del GET
def test_GetUserPlaylists_clase_5():
    url = 'https://playstack.azurewebsites.net/get/playlists?NombreUsuario=Freeman'
    request = requests.post(url)
    assert request.status_code == 405


def test_GetRandomAlbums_clases_validas():
    url = 'https://playstack.azurewebsites.net/get/randomalbums'
    request = requests.get(url)
    assert request.status_code == 200

# Se utiliza un metodo POST en lugar del GET
def test_GetRandomAlbums_clase_2():
    url = 'https://playstack.azurewebsites.net/get/randomalbums'
    request = requests.post(url)
    assert request.status_code == 405

def test_RemoveAudio_clases_validas():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'NombreUsuario': '', 'Titulo': ''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['Titulo'] = 'Test'
    request = requests.post(url, json=datos)
    assert request.status_code == 400
'''

######################################################################################
#################################### LOGIN TEST ######################################
######################################################################################
'''
def test_Login_clases_validas():

    url = 'https://playstack.azurewebsites.net/user/login'
    datos = {'NombreUsuario': '', 'Contrasenya': ''}

    datos['NombreUsuario'] = 'ErTisho'
    datos['Contrasenya'] = 'cacahuete1'
    request = requests.post(url, json=datos)
    assert request.status_code == 200

def test_Login_clase_4():

    url = 'https://playstack.azurewebsites.net/user/login'
    datos = {'NombreUsuario': '', 'Contrasenya': ''}

    datos['NombreUsuario'] = 'ErTishoTPM'
    datos['Contrasenya'] = 'cacahuete1'
    request = requests.post(url, json=datos)
    assert request.status_code == 404

def test_Login_clase_5():
    url = 'https://playstack.azurewebsites.net/user/login'
    datos = {'Contrasenya': ''}
    datos['Contrasenya'] = 'cacahuete1'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

def test_Login_clase_6():

    url = 'https://playstack.azurewebsites.net/user/login'
    datos = {'NombreUsuario': '', 'Contrasenya': ''}

    datos['NombreUsuario'] = 'ErTisho'
    datos['Contrasenya'] = 'cacahuete12325'
    request = requests.post(url, json=datos)
    assert request.status_code == 401

def test_Login_clase_7():

    url = 'https://playstack.azurewebsites.net/user/login'
    datos = {'NombreUsuario': ''}

    datos['NombreUsuario'] = 'ErTisho'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

def test_Login_clase_8():

    url = 'https://playstack.azurewebsites.net/user/login'
    datos = {'NombreUsuario': '', 'Contrasenya': ''}

    datos['NombreUsuario'] = 'ErTisho'
    datos['Contrasenya'] = 'cacahuete12325'
    request = requests.get(url, json=datos)
    assert request.status_code == 405
'''
######################################################################################
############################ FOLLOWREQUESTS TEST #####################################
######################################################################################
'''
def test_followRequest_clases_validas():
    url = 'https://playstack.azurewebsites.net/user/get/followrequests'

    url=url + '?Usuario=ErTisho'
    request = requests.get(url)
    assert request.status_code == 200

def test_followRequest_clase_3():

    url = 'https://playstack.azurewebsites.net/user/get/followrequests'

    url=url + '?Usuario=ErTishoTTTPM'
    request = requests.get(url)
    assert request.status_code == 404

def test_followRequest_clase_4():

    url = 'https://playstack.azurewebsites.net/user/get/followrequests'

    #url=url + '?NombreUsuario=ErTishoTTTPM'
    request = requests.get(url)
    assert request.status_code == 400

def test_followRequest_clase_5():

    url = 'https://playstack.azurewebsites.net/user/get/followrequests'

    url=url + '?Usuario=ErTisho'
    request = requests.post(url)
    assert request.status_code == 405
'''

######################################################################################
############################ ADDSONGTOLISTENED TEST ##################################
######################################################################################
def test_AddSongToListened_clases_validas():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTisho'
    datos['Titulo'] = 'So Payaso'
    datos['Timestamp'] = '1999/10/26 00:00:00'
    request = requests.post(url, json=datos)
    assert request.status_code == 200

def test_AddSongToListened_clase_5():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTishoTPM'
    datos['Titulo'] = 'So Payaso'
    datos['Timestamp'] = '1999/10/26 00:00:00'
    request = requests.post(url, json=datos)
    assert request.status_code == 404

def test_AddSongToListened_clase_6():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}


    datos['Titulo'] = 'So Payaso'
    datos['Timestamp'] = '1999/10/26 00:00:00'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

def test_AddSongToListened_clase_7():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTisho'
    datos['Titulo'] = 'So Payasete XD'
    datos['Timestamp'] = '1999/10/26 00:00:00'
    request = requests.post(url, json=datos)
    assert request.status_code == 404

def test_AddSongToListened_clase_8():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTisho'
    datos['Timestamp'] = '1999/10/26 00:00:00'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

def test_AddSongToListened_clase_9():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTisho'
    datos['Titulo'] = 'So Payasete XD'
    datos['Timestamp'] = 'MAS VINAGRE 1999/10/26 00:00:00 EN VINAGRE'
    request = requests.post(url, json=datos)
    assert request.status_code == 404

def test_AddSongToListened_clase_10():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTisho'
    datos['Titulo'] = 'So Payasete XD'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

def test_AddSongToListened_clase_10():

    url = 'https://playstack.azurewebsites.net/user/add/song/tolistened'
    datos = {}

    datos['Usuario'] = 'ErTisho'
    datos['Titulo'] = 'So Payasete XD'
    request = requests.get(url, json=datos)
    assert request.status_code == 405
# El usuario no existe
def test_RemoveAudio_clase_7():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'NombreUsuario': '', 'Titulo': ''}

    datos['NombreUsuario'] = 'usuario_test'
    datos['Titulo'] = 'Test'
    request = requests.post(url, json=datos)
    assert request.status_code == 404

# El usuario no es creador
def test_RemoveAudio_clase_8():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'NombreUsuario': '', 'Titulo': ''}

    datos['NombreUsuario'] = 'Pedro14'
    datos['Titulo'] = 'Test'
    request = requests.post(url, json=datos)
    assert request.status_code == 401

# El audio no existe
def test_RemoveAudio_clase_9():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'NombreUsuario': '', 'Titulo': ''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['Titulo'] = 'audio_test'
    request = requests.post(url, json=datos)
    assert request.status_code == 404

# No existe el campo NombreUsuario
def test_RemoveAudio_clase_10():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'Titulo': ''}
    datos['Titulo'] = 'Test'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

# No existe el campo Titulo
def test_RemoveAudio_clase_11():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'NombreUsuario': ''}
    datos['NombreUsuario'] = 'DiosCreador'
    request = requests.post(url, json=datos)
    assert request.status_code == 400

# Se utiliza un metodo GET en lugar del POST
def test_RemoveAudio_clase_12():

    url = 'https://playstack.azurewebsites.net/audio/remove'
    datos = {'NombreUsuario': '', 'Titulo': ''}
    datos['NombreUsuario'] = 'DiosCreador'
    datos['Titulo'] = 'Test'
    request = requests.get(url, json=datos)
    assert request.status_code == 405

def test_CreateAlbum_clases_validas():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '2020/09/09'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, data=datos, files=files)
    assert request.status_code == 200

# El usuario no existe
def test_CreateAlbum_clase_8():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreUsuario'] = 'usuario_test'
    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '2020/09/09'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, data=datos, files=files)
    assert request.status_code == 404

# El usuario no tiene permisos
def test_CreateAlbum_clase_9():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreUsuario'] = 'Pedro14'
    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '2020/09/09'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, data=datos, files=files)
    assert request.status_code == 401

# El campo  NombreUsuario no existe
def test_CreateAlbum_clase_10():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreAlbum': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '2020/09/09'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, json=datos, files=files)
    assert request.status_code == 400

 # El campo NombreAlbum no existe
def test_CreateAlbum_clase_11():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['Fecha'] = '2020/09/09'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, data=datos, files=files)
    assert request.status_code == 400

# El campo Fecha no existe
def test_CreateAlbum_clase_12():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': ''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreAlbum'] = 'album_test'
    datos['NombreUsuario'] = 'DiosCreador'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, data=datos, files=files)
    assert request.status_code == 400

# El campo FotoDelAlbum no existe
def test_CreateAlbum_clase_13():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': '','Fecha':''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '2020/09/09'

    request = requests.post(url, json=datos)
    assert request.status_code == 400

# Formato de fecha erroneo
def test_CreateAlbum_clase_14():

    url = 'http://127.0.0.1:8000/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '20/09/2009'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.post(url, json=datos, files=files)
    assert request.status_code == 400

# Se utiliza un metodo GET en lugar del POST
def test_CreateAlbum_clase_15():

    url = 'https://playstack.azurewebsites.net/create/album'
    datos = {'NombreUsuario': '', 'NombreAlbum': '','Fecha':''}
    files = {'FotoDelAlbum' : ''}

    datos['NombreUsuario'] = 'DiosCreador'
    datos['NombreAlbum'] = 'album_test'
    datos['Fecha'] = '2020/09/09'
    files['FotoDelAlbum'] = open('Imagen5.png' , 'rb')

    request = requests.get(url, data=datos, files=files)
    assert request.status_code == 405