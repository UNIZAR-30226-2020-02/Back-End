# Deficnicion de los metodos disponibles por RCP

from modernrpc.core import rpc_method

@rpc_method
def hello():
    return 'Hello world!'