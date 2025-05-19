from animal import Animal


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

class Caballo(Animal):
    def carga(self, kilos):
        print(f"El Caballo {self.nombre} está cargando peso de {kilos} kilos")
        if kilos > 50:
            print("¡Carga excesiva!")   
