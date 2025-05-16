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