import os

"""
    Manejo de Ficheros
"""

file_name = "qupi.txt"

with open(file_name, "w") as file:
    file.write("Qupi\n")
    file.write("36\n")
    file.write("Python")


with open(file_name, "r") as file:
    print(file.read())

os.remove(file_name)

file_name = "qupi_shop.txt"

while True:
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Borrar Producto")
    print("5. Calcular venta Total")
    print("6. Calcular venta por producto")
    print("7. Mostrar Productos")
    print("8. Salir")

    option = input("Selecciona una opcion: ")

    match option:
        case "1":
            name = input("Nombre del Producto: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "a") as file:
                file.write(f"{name},{quantity},{price} \n")
        case "2":
            name = input("Nombre: ")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(',')[0] == name:
                        print(line)
                        break
        case "3":
            name = input("Nombre del Producto: ")
            quantity = input("Cantidad: ")
            price = input("Precio: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(',')[0] == name:
                        file.write(f"{name},{quantity},{price} \n")
                    else:
                        file.write(line)

        case "4":
            name = input("Nombre del Producto: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(',')[0] != name:
                        file.write(line)
        case "5":
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(",")
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
            print(total)
        case "6":
            name = input("Nombre del Producto: ")
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(",")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
            print(total)
        case "7":
            with open(file_name, "r") as file:
                print(file.read())
        case "8":
            os.remove(file_name)
            break
        case _:
            print("Selecciona una de las opciones disponibles")