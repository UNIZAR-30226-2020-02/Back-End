# Fichero donde se declaran los distintos recursos que
# seran accedidos mediante peticiones


from tastypie.resources import ModelResource
from playstackDjango.App.PlayStack.models import *

# Devuelve todos los usuarios existentes en la base de batos
# en fromato JSON
class UsuarioResource(ModelResource):
    class Meta:
        queryset = Usuario.objects.all()
        resource_name = 'usuario'