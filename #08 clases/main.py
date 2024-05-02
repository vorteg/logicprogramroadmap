"""
    Clases

"""

class Animal:
    def __init__(self,patas) -> None:
        self.patas:int = patas

    def run(self):
        print(f"corre en su {self.patas} patas")

perro = Animal(4)
perro.run()



class Pila:
    def __init__(self) -> None:
        self.pila = []

    def adding(self,element):
        self.pila.append(element)
        print(self.pila)
    
    def delete(self):
        self.pila.pop()
        print(self.pila)
    
p = Pila()
p.adding("test")
p.adding("2")
p.adding("otro")

p.delete()
