# -*- coding: utf-8 -*-

# Creación de un Chat Cliente Servidor Usando Sockets en Python
import socket
import funciones_servidor


def main():
    servidor = socket.socket()
    servidor.bind(("", 5000))
    servidor.listen(1)
    socket_cliente, datos_conexion = servidor.accept()

    usuario = False
    contrasena = False
    menu = False

    while True:


        #mensaje_servidor = raw_input("Ingrese Respuesta al Cliente >> ")
        contador = 0


        #validar usuario
        while(usuario != True):
            if(contador > 0):
                mensaje_servidor = funciones_servidor.getusuario_error()
                socket_cliente.send(mensaje_servidor)

            mensaje_servidor = funciones_servidor.getusuario()
            socket_cliente.send(mensaje_servidor)
            mensaje_cliente = socket_cliente.recv(1024)

            if(funciones_servidor.validar_usuario(mensaje_cliente)):
                usuario = True

            contador = contador + 1

        #validar contraseña
        contador = 0
        while (contrasena != True):
            if (contador > 0):
                mensaje_servidor = funciones_servidor.getcontrasena_error()
                socket_cliente.send(mensaje_servidor)

            mensaje_servidor = funciones_servidor.getcontrasena()
            socket_cliente.send(mensaje_servidor)
            mensaje_cliente = socket_cliente.recv(1024)

            if (funciones_servidor.validar_contrasena(mensaje_cliente)):
                contrasena = True

            contador = contador + 1

        contador = 0
        if(menu != True and contrasena == True):
            while(True):
                if (contador > 0):
                    mensaje_servidor = funciones_servidor.getmenu_error()
                    socket_cliente.send(mensaje_servidor)

                mensaje_servidor = funciones_servidor.menu()
                socket_cliente.send(mensaje_servidor)
                mensaje_cliente = int(socket_cliente.recv(1024))
                if(mensaje_cliente > 0 and mensaje_cliente < 6):
                    menu = True
                    break

                contador += 1


        operacion = mensaje_cliente

        if(menu == True):
            mensaje_servidor = funciones_servidor.getnum_1()
            socket_cliente.send(mensaje_servidor)
            num_1 = int(socket_cliente.recv(1024))
            mensaje_servidor = funciones_servidor.getnum_2()
            socket_cliente.send(mensaje_servidor)
            num_2 = int(socket_cliente.recv(1024))
            if(operacion == 1):
                mensaje_servidor = funciones_servidor.suma(num_1, num_2)
                socket_cliente.send(mensaje_servidor)
                menu = False

        if (menu == True):
            mensaje_servidor = funciones_servidor.getnum_1()
            socket_cliente.send(mensaje_servidor)
            num_1 = int(socket_cliente.recv(1024))
            mensaje_servidor = funciones_servidor.getnum_2()
            socket_cliente.send(mensaje_servidor)
            num_2 = int(socket_cliente.recv(1024))
            if (operacion == 2):
                mensaje_servidor = funciones_servidor.resta(num_1, num_2)
                socket_cliente.send(mensaje_servidor)
                menu = False

    print "Hasta Pronto"
    socket_cliente.close()
    servidor.close()

if __name__ == '__main__':
    main()