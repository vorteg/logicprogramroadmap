"""
    Valor y referencia
"""

# Tipos de dato por valor
my_int_a = 10
#my_int_b = 20
my_int_b = my_int_a
my_int_a = 30

print(my_int_a)
print(my_int_b)# b conserva el primer valor asignado

# Tipos de dato por referencia
#Todos los que no son primitivos
my_list_a = [10,20]
#my_list_b = [30,40]
my_list_b = my_list_a
#my_list_a = [50,10] #Aqui no se modifica se crea una nueva instancia en memoria
my_list_b.append(15)
print(my_list_a)
print(my_list_b)#No copia valor lo hereda va a apuntar a la misma direccion 
# a menos de que se vuelva a definir la variable

my_list_d = my_list_a.copy()
my_list_d.append(67)
print(my_list_d)

#Funciones con datos por valor
my_var_test = "test"
print(f"antes de funcion {my_var_test}")

def test_var_val(my_var):
    print(my_var)
    my_var = 123
    print(my_var)
    global my_var_test 
    my_var_test = "si se modifico"

test_var_val(my_var_test)
print(f"despues de funcion {my_var_test}")

#Funciones con datos por referencia

def test_list(my_list:list):
    my_list.append(89)# en este caso estamos trabajando con la referencia
    print(my_list)

def test_list_no_ref(my_list:list):
    my_no_ref_list = my_list.copy()
    my_no_ref_list.append(19)# en este caso estamos trabajando con la referencia
    print(my_no_ref_list)

test_list(my_list_a)
print(my_list_a)
test_list_no_ref(my_list_a)