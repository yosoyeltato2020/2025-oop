def caosZoologico():
    mapachio = Animal("Mapachio")
    print(isinstance(mapachio, Animal))
    print(isinstance(mapachio, Perro))
    mapachio.come()

    firulais = Perro("Firulais")
    firulais.come()
    firulais.pasea()

    myLittle = Pony("My Little")
    myLittle.come()
    myLittle.pasea()


# Definimos una clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def come(self):
        print(f"El Animal {self.nombre} ha comido")


# la Super Clase de Domestico es Animal
# Perro es Sub Clase de Domestico
# Domestico es Super Clase de Perro
# Domestico es Sub clase de Animal
class Domestico(Animal):
    def pasea(self):
        print(f"El Animal domestico {self.nombre} se pasea")


# Creamos una clase hija que hereda de la padre
class Perro(Domestico):
    pass


class Pony(Domestico):
    pass


if __name__ == "__main__":
    caosZoologico()
