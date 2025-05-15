import random


class Traje:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Traje de color: {self.color}"


# Composición: Los atributos del Guerrero son otro objeto
class Guerrero:
    def __init__(self, color, id, vida):
        self.color = color
        self.id = id
        self.vida = vida

    def presentar(self):
        return f"Soy el ranger {self.color}"

    def herir(self, cantidad=1):
        self.vida -= cantidad
        if self.vida <= 0:
            print(f" * El guerrero {self.color} se ha muerido")
        else:
            print(f" * Al guerrero {self.color} aun le quedan {self.vida} vidas")


class Juego:
    def __init__(self):
        self.rangers = []

        self.crear()
        self.presentar()
        self.pelear()

    def crear(self):
        colores = [
            Traje("rojo"),
            Traje("verde"),
            Traje("azul"),
            Traje("amarillo"),
            Traje("rosa")
        ]

        for i in range(5):
            self.rangers.append(Guerrero(color=colores.pop(0), id=i, vida=3))

        return self.rangers

    def presentar(self):
        for ranger in self.rangers:
            print(ranger.presentar())

    def pelear(self):
        for _ in range(3):
            for ranger in self.rangers:
                if random.randint(0, 1) == 1:
                    ranger.herir()

        self.rangers[3].herir(5)

        for ranger in self.rangers:
            if ranger.vida <= 0:
                print(f"El ranger {ranger.id} esta muerido")


Juego()
