"""Cadena de Caracteres"""

# Cadena de ejemplo
cadena = "Hola, mundo!"

# Acceso a caracteres específicos
print(cadena[0])  # H
print(cadena[-1])  # !

# Subcadenas
print(cadena[2:6])  # la, 

# Longitud de la cadena
print(len(cadena))  # 12

# Concatenación de cadenas
otra_cadena = " Qué tal?"
print(cadena + otra_cadena)  # Hola, mundo! Qué tal?

# Repetición de cadenas
print(cadena * 3)  # Hola, mundo!Hola, mundo!Hola, mundo!

# Recorrido de caracteres
for caracter in cadena:
    print(caracter)

# Conversión a mayúsculas y minúsculas
print(cadena.upper())  # HOLA, MUNDO!
print(cadena.lower())  # hola, mundo!

# Reemplazo
print(cadena.replace("mundo", "amigo"))  # Hola, amigo!

# División
print(cadena.split(","))  # ['Hola', ' mundo!']

# Unión
palabras = ["Hola", "mundo"]
print(" ".join(palabras))  # Hola mundo

# Interpolación
nombre = "Juan"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Mi nombre es Juan y tengo 30 años.

# Verificación
print("mundo" in cadena)  # True
print("hola" not in cadena)  # True

def analize_word(text_1:str, text_2:str)-> None:
        print(text_1, text_2)
        print("Son  palindromos") if text_1  == text_1[::-1] and text_2  == text_2[::-1] else print("no palindromos")
        print("Son anagramas") if sorted(text_1) == sorted(text_2) else print("No son anagramas") 
        print("Son Isogramas") if len(text_1) == len(set(text_1)) and len(text_1) == len(set(text_1)) else print("No son Isogramas") 
        
analize_word("radar", "abba")
analize_word("amor", "roma")
analize_word("fenix", "submarino")