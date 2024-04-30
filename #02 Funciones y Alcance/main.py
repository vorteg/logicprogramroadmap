# Diferentes tipos de funciones

def print_warning() -> None:
    #  Sin parámetros ni retorno
    print("Advertencia")

def adding_numbers(a:int,b:int) -> None:
    # con uno o varios parámetros
    print("Funcion 2")
    print(f"Este es el resultado de a + b {a+b}")

def adding_return(a:int,b:int)-> int:
    # con retorno
    print("Funcion 3")
    print(f"Regresa el resultado de a + b")
    return a + b

def nest_function(a:int) -> None:
    print("Funcion 4")
    print(f"Esto vale a:{a}")
    print(f"este es el valor recibido + 1 = {a+1}")
    def multiply_by_2():
        print(f"Funcion anidada,se multiplica el valor a * 2 = {a*2}")
    multiply_by_2()

#Variable global
CONSTANT = 15

def scope_var():
    local_var = 3
    print(f"Accediendo a Variable global {CONSTANT}")

try:
    print(f"Tratando de acceder a variable local{local_var}")
except:
    print("No se pudo acceder desde fuera de la funcion a local_var")

print_warning()
adding_numbers(1 ,4)
print(adding_return(2,6))
nest_function(2)

def challenge(text:str,text2:str) -> int:
    count = 0
    for i in range(1,100):
        if i % 3 == 0 and  i % 5 == 0:
             print(f"{text+text2}")
        elif i % 3 == 0:
            print(f"{text}")
        elif i % 5 == 0:
            print(f"{text2}")
        else:
            print(i)
            count =+ 1
        
    return count

challenge("Fizz","Buzz")