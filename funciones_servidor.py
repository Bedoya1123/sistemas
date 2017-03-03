# -*- coding: utf-8 -*-
import json

def menu():
    lista = ["Bienvenido a la Calculadora", "1. Suma", "2. Resta", "3. Multiplicar", "4. División", "5. Salir", "Digite el número de la opción >>"]
    cadena = json.dumps(lista)
    return cadena

def getusuario():
    lista = ["Ingrese su Usuario >>"]
    cadena = json.dumps(lista)
    return cadena

def getcontrasena():
    lista = ["Ingrese su Contraseña >>"]
    cadena = json.dumps(lista)
    return cadena

def validar_usuario(cadena):
    if(cadena == "cristian"):
        return True
    else:
        return False

def validar_contrasena(cadena):
    if(cadena == "cristian"):
        return True
    else:
        return False

def getusuario_error():
    lista = ["Usuario incorrecto", "Presione enter para intentarlo de nuevo >>"]
    cadena = json.dumps(lista)
    return cadena

def getcontrasena_error():
    lista = ["Contraseña incorrecta", "Presione enter para intentarlo de nuevo >>"]
    cadena = json.dumps(lista)
    return cadena

def getmenu_error():
    lista = ["Opcion Invalida", "\n", "Presione enter para mostrar el menu de nuevo"]
    cadena = json.dumps(lista)
    return cadena

def getnum_1():
    lista = ["Ingese el numero 1 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def getnum_2():
    lista = ["Ingese el numero 2 y presione enter >>"]
    cadena = json.dumps(lista)
    return cadena

def suma(num1, num2):
    suma = str(num1 + num2)
    lista = ["Resultado de la operacion = " + suma, "Presione enter para volver al menu"]
    cadena = json.dumps(lista)
    return cadena

def resta(n1,n2):
    resp=int(n1)-int(n2)
    return str(resp)

def multi(n1,n2):
    resp=int(n1)*int(n2)
    return str(resp)

def div(n1,n2):
    resp=float(n1)/float(n2)
    return str(resp)