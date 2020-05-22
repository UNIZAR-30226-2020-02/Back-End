import requests
import json

url = 'http://127.0.0.1:8000/create/song'

datos = dict.fromkeys({'NombreUsuario', 'Titulo', 'Duracion', 'Idioma','Artistas', 'Generos','NombreAlbum'})
d = {'uno': 'j'}
datos['NombreUsuario'] = 'DiosCreador'
datos['Titulo'] = 'CancionRemotaBien'
datos['Duracion'] = 6.45
datos['Idioma'] = 'Ingles'
datos['Artistas'] = 'Guille Placencia'
datos['NombreAlbum'] = 'Logic'
datos['Generos'] =  'Pop,Dance'
headers = {'content-type': 'application/json'}
file = {'FicheroDeAudio' : open('Eminem - Rap God.mp3' , 'rb')}
headers = {'content-type': 'application/json'}
request = requests.post(url, data=datos,files=file
#,headers=headers
)

if request.status_code == 200:
    print('Peticion atendida correctamente')

else:

    print('Error recivido: ', request.status_code)
    print(request.json())
