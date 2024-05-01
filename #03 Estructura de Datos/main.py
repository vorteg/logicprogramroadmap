"Estructura de Datos"

lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
conjunto = {1, 2, 3, 4, 5}
diccionario = {'clave1': "valor1", 'clave2': "valor2"}

#Poco comunes
from collections import deque

cola = deque([1, 2, 3])

##################################3
import heapq

cola_prioridad = []
heapq.heappush(cola_prioridad, 5)
heapq.heappop(cola_prioridad)
###############################3
conjunto_inmutable = frozenset({1, 2, 3})
###########################33333

from collections import Counter

lista = ['a', 'b', 'a', 'c', 'b', 'a']
contador = Counter(lista)
print(contador)
##################################3
from collections import OrderedDict

diccionario_ordenado = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

import os

def agenda():
    contactos = []
    def search():
        keyword = input("Ingrese el nombre del contacto a buscar")
        if keyword in contactos:
            print(contactos[keyword])
        else:
            print("contacto no  encontrado")
    def adding():
        name = input("Ingrese el nombre:")
        numero = int(input("Ingrese el numero:") )   
        contacto = {
            "nombre":name,
            "numero":numero
        }
        contactos.append(contacto)
        print(contactos)

    def update():
        name = input("ingrese el nombre del contacto:")
        edit = int(input("1) actualizar nombre, 2) actualizar numero:"))
        if edit == 1:
            new_name = input("ingrese nuevo nombre")
            contactos[name]["nombre"] = new_name
        else:
            new_number = input("ingrese nuevo numero")
            contactos[name]["numero"] = int(new_number)
        print(contactos)

    def delete():
        name = input("ingrese el nombre del contacto:")
        contactos.remove(name)
        print(contactos)

    while True:
        print("Operacion gusta realizar?")
        resp = int(input("1) Buscar contacto \n 2) Agregar contacto \n 3) Actualizar contacto \n  4) Eliminar contacto \n"))
        if resp == 1:
            search()
        elif resp == 2:
            adding()
        elif resp == 3:
            update()
        elif resp == 4:
            delete()
        else:
            print("Operacion no reconocida, elija del 1 al 4")
        resp = input("Deseas realizar alguna otra operacion si/no?")
        if resp != "si" :
            break
        os.system("clear")


agenda()