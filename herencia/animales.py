# from random import randint
from random import *
import random
from animal import Animal


def randint(a, b):
    return "PATATA"


print(randint(100, 200))
print(random.randint(100, 200))








exit()


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def pasea(self):
        print(f"El Perro {self.raza} llamado {self.nombre} se pasea")

    def come(self):
        super().come()


# Larva sobrescribe el método
class Larva(Animal):
    def come(self):
        self.comidas += 0.1
        print("Me fabrica seda")
        print("La Larva SE TRANFORMA en mariposa")


# Gremiln EXTIENDE el método
class Gremlin(Animal):
    def come(self):
        super().come()                  # Primero ejecuta el comportamiento del super
        print("Gremlin se TRANSFORMA")  # Luego expande la funcionalidad


class Caballo(Animal):
    def __init__(self, nombre, carga_maxima=100):
        super().__init__(nombre)
        self.carga_maxima = carga_maxima

    def carga(self, kilos):
        if kilos > self.carga_maxima:
            print(f"¡Carga excedida! {self.nombre} solo puede cargar hasta {self.carga_maxima} kilos")
        else:
            print(f"El Caballo {self.nombre} está cargando {kilos} kilos")


class Caballo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.max = 30
        self.peso = 0

    def transportar(self, destino):
        print(f"El caballo transportó la carga a {destino}")

    def cargar(self, peso):
        if peso > self.max:
            print(f"{self.nombre} se niega a cargar ({peso}) kilos")
            return False
        self.peso = peso
        return True

    def descargar(self):
        return self.peso



if __name__ == "__main__":
    perrito = Perro("Perry Poppins", "Pug")
    for i in range(random.randint(1, 10)):
        perrito.come()
>>>>>>> 50d1faf0c50c94a7967bb55e07098e26fa97a316
