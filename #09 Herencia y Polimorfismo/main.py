"""
    Herencia y Polimorfismo
"""


#Definir una clase Padre
class Animal:
    def __init__(self,nombre:str) -> None:
        self.name = nombre

    def sound(self):
        ...

#Definir nuevas clases
class Dog(Animal):

    def sound(self):
        print(f"{self.name} dice Wua Wua!")


#Definir otra clase que herede al padre

class Cat(Animal):
    #Al sobre escribir una funcion ya estamos trabajando con 
    #Polimorfismo compilado
    def sound(self):
        print(f"{self.name} dice Miau!")


def get_sound(animal:Animal):
    animal.sound()


my_cat = Cat("Gato")
my_dog = Dog("Perro")

#Esto es polimorfismo en ejecucion el comportamiento 
#Cambiara segun el objeto
get_sound(my_cat)
get_sound(my_dog)
