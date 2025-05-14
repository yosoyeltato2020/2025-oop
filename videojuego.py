import random

colores = ["rojo", "verde", "azul", "amarillo", "rosa"]


class Guerrero:
    def __init__(self):
        self.color = colores.pop()
        self.vida = 3

    def presentar(self):
        return f"Soy el ranger {self.color}"

    def herir(self):
        self.vida -= 1
        if self.vida <= 0:
            print(f" * El guerrero {self.color} se ha muerido")
        else:
            print(f" * Al guerrero {self.color} aun le quedan {self.vida} vidas")


rangers = []
for i in range(5):
    rangers.append(Guerrero())

for ranger in rangers:
    print(ranger.presentar())

for _ in range(3):
    for ranger in rangers:
        if random.randint(1, 1) == 1:
            ranger.herir()
