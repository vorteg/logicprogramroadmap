"""
    Operadores
"""

#operadores aritmeticos
suma = 1 + 2
otra_suma = 0
otra_suma += 1
resta = 5-1
multiplicar = 2*3
potencia = 2**3
#Operadores booleanos
operador_and = 1 and 1
operador_or = 0 or 1
operador_xor = False ^ False
operador_not = not True
print(operador_xor)


#Operadores bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010 == 2
print(f"OR: 10 | 3 = {10 | 3}") # 1011 == 11
print(f"XOR: 10 ^ 3 = {10 ^ 3}")# 1001 == 9
print(f"NOT: ~10 = {~10}") # -1011 == -11
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 1010 >> 2bits == 0010 == 2
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 1010 << 2bits == 101000 == 40

#Estructura de control

my_string =  "test"

if my_string == "test":
    print(my_string)
elif  my_string == "otro":
    print("era otro")
else:
    print("my_string no existe")

#iterativas
for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

#Manejo de excepciones
try:
    print(10/0)
except:
    print("se ha producido un error")

finally:
    print("Ha finalizado  el manejo de error")

for i in range(10,55):
    if i % 2 == 0 and i != 16:
        if i % 3 == 0:
            continue
        print(i)