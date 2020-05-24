#!/usr/bin/env python2

from __future__ import print_function
import sys
sys.path.insert(1, '/usr/local/lib/python3.8/dist-packages/')

import pytest
import requests
import json

def test_uno():
    url = 'https://playstack.azurewebsites.net/create/user'
    headers = {'content-type': 'application/json'}
    datos = {'NombreUsuario' : '', 'Contrasenya' : '', 'Correo' : ''}

    datos['NombreUsuario'] = 'federicoLorca'
    datos['Correo'] = 'f@gamil.com'
    datos['Contrasenya'] = 'password'

    request = requests.post(url, data=datos,headers=headers)
    print(request.status_code)
    assert request.status_code == 200
