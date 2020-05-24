import requests
import json

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

get/song/byartist