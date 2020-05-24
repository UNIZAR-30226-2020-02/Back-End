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
    print(request.status_code)
    assert request.status_code == 201

def test_CreateUser_clase7():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca'
    datos['Correo'] = 'fe@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, json=datos)
    print(request.status_code)
    assert request.status_code == 201
