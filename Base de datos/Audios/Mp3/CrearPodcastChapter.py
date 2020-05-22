import requests
import json

url = 'http://127.0.0.1:8000/create/podcastchapter'

datos = dict.fromkeys({'NombreUsuario', 'Titulo', 'Duracion', 'Idioma', 'Fecha','NombrePodcast','Interlocutores'})

datos['NombreUsuario'] = 'DiosCreador'
datos['Titulo'] = 'CancionRemotaBien'
datos['Duracion'] = 6.45
datos['Idioma'] = 'Ingles'
datos['Fecha'] =  '2020/05/22'
datos['Interlocutores'] = 'Enrique Torres'
datos['NombrePodcast'] = 'Speak English now'
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
