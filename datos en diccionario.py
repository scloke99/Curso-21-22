# Ejercicio 1 :

# Programa que pida al usuario los siguientes datos:
# -nombre
# -apellido
# -Fecha nacimiento
# -Telefono

# tiene que pedir los datos hasta que el usuario diga que ya termino

# los datos se guardan en un diccionario

# al final se muestra el diccionario



import os
import pprint


def datos_personales():
    datos = {}
    for i in range(10):
        
        nombres = input("introduzca su nombre: ")
        apellidos = input("introduzca su apellido: ")
        Fechas_de_nacimientos = input("introduzca su fecha de nacimiento: ")
        Telefonos = input("introduzca su telefono: ")
        dni = input("introduzca su DNI: ")
        querer_seguir = input("¿Quieres seguir?: SI/NO ")
        datos[dni] = {"Nombre":nombres, "apellidos": apellidos, "fechas": Fechas_de_nacimientos, "telefonos": Telefonos, "seguir": querer_seguir, "DNI": dni}

        if querer_seguir == "SI":
            pass
        elif querer_seguir == "NO":
            break 
        
    return datos

pprint.pprint(datos_personales())
