import json

def menu():
    lista = ["Bienvenidos al supermercado","1.comprar productos", "2.ventas del dia", "3.inventarios", "4.salir"]
    cadena = json.dumps(lista)
    return cadena

def comprar_productos():
    lista = ["1. Frijoles   $ 2500","1.comprar productos", "2.ventas del dia", "3.inventarios", "4.salir"]
    cadena = json.dumps(lista)
    return cadena


def ventas_dia():
    cadena = "ventas dia"
    return cadena

def inventarios():
    cadena = "inventarios"
    return cadena

