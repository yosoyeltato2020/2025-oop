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
<<<<<<< HEAD
        self.vida = vida
        self.vida_max = 3
=======
        self.vida_max = vida
        self.vida = self.vida_max
>>>>>>> 8a7707308671eebcb62b60c7700956bca52b6f46

    def presentar(self):
        return f"Soy el ranger {self.color} y tengo {self.vida} vidas"

    def herir(self, cantidad=1):
        self.vida -= cantidad
        if self.vida <= 0:
            print(f" * El guerrero {self.color} se ha muerido")
        else:
            print(f" * Al guerrero {self.color} aun le quedan {self.vida} vidas")
    def descansar(self):
        if self.vida <= 0:
            return f"El guerrero {self.color} esta descansando ETERNAMENTE"
        if self.vida < 3:
            self.vida = 3
        return f"el guerrero {self.color} ha descansado"

<<<<<<< HEAD
    
=======
    def descansar(self):
        if self.vida <= 0:
            return f"El Guerrero {self.color} esta descansando ETERNAMENTE"

        if self.vida < self.vida_max:
            self.vida = self.vida_max

        return f"El Guerrero {self.color} ha descansado"

>>>>>>> 8a7707308671eebcb62b60c7700956bca52b6f46

class Juego:
    def __init__(self):
        self.rangers = []

        self.crear()
        self.presentar()
        self.pelear()
        self.descansar()
<<<<<<< HEAD
=======
        self.presentar()
>>>>>>> 8a7707308671eebcb62b60c7700956bca52b6f46

    def crear(self):
        colores = [
            Traje("rojo"),
            Traje("verde"),
            Traje("azul"),
            Traje("amarillo"),
            Traje("rosa")
        ]

        for i in range(5):
            color = colores.pop(0)
            vida = 3
            self.rangers.append(Guerrero(color=color, id=i, vida=vida))
            # self.rangers.append(Guerrero(color, i, vida))

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
    
    def descansar(self):
        for ranger in self.rangers:
            if ranger.vida > 0:
                ranger.vida = ranger.vida_max
                print(f"El ranger {ranger.id} ha descansado y ahora tiene {ranger.vida} vidas")
            else:
                print(f"El ranger {ranger.id} no puede descansar porque está muerto")


    def descansar(self):
        print("Los Rangers descansan:")
        for ranger in self.rangers:
            print(ranger.descansar())


Juego()
