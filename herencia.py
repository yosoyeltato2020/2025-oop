def caosZoologico():
    firulais = Perro("Firulais", "ChowChow")
    firulais.come()
    firulais.pasea()

    mizgo = Larva("Mizgo")
    mizgo.come()

    gizmo = Gremlin("Gizmo")
    gizmo.come()

    firulais.registrar()
    gizmo.registrar()


# Definimos una clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.comidas = 0
        self.chip = 1234654

    def come(self):
        self.comidas += 1
        print(f"El Animal {self.nombre} ha comido {self.comidas} veces")

    def registrar(self):
        print(f"Hemos registado a {self.nombre} en la BBDD del gobierno")


class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def pasea(self):
        print(f"El Perro {self.raza} llamado {self.nombre} se pasea")


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


if __name__ == "__main__":
    caosZoologico()
