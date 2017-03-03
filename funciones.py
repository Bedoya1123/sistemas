import json
def menu():
    lista = ["1. Iniciar Sesion", "2. Salir"]
    cadena = json.dumps(lista)
    return cadena

def menu_lista(cadena):
    lista = json.loads(cadena)
    for i in lista:
        print i

def iniciar_sesion():
    pass