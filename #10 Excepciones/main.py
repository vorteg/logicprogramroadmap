"""
     Manejo de Errores
"""

# try:
#     print(10/1) # 10/0
#     my_list = [1,2,3]
#     print(my_list[5]) # FOrzando el error
# except Exception as e:
#     print(f"Se ha producido un error: {e} ({type(e).__name__})")


"""
    Extra
"""

class StrTypeError(Exception):
    ...

def process_params(parameters:list):
    
    if len(parameters) < 3:
        raise IndexError()
    elif parameters[1] == 0:
        raise ZeroDivisionError()
    elif type(parameters[2]) == str:
        raise StrTypeError("No se debe agregar datos de tipo string")
    
    print(parameters[2])
    print(parameters[0]/parameters[1])


try:
    process_params([1,2,3,4])
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor a dos.")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser un cero.")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido in error inesperado: {e} ({type(e).__name__})")
else:
    print("No se ha producido ningun error.")
finally:
    print("programa finalizado")