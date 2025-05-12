print("Hola Patoburgo")


class Pato:
    def __init__(self, nombre="ANONIMO"):
        print("CUACK")
        self.nombre = nombre
        self.plumas = 3
        self.presentarse()

    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.plumas} plumas")

    def irse_a_casa(self):
        print(f"{self.nombre} se va a casa")

        return self.plumas


pato1 = Pato("Juanito McPato")
pato2 = Pato("Jorgito McPato")
pato3 = Pato()
pato3.plumas += 17
pato3.presentarse()
pato4 = Pato("Iratxe Pato")

patociudadanos = []

for i in range(4):
    patociudadanos.append(Pato(f"Extra {i}"))

patociudadanos.append(pato1)
patociudadanos.append(pato2)
patociudadanos.append(pato3)
patociudadanos.append(pato4)


plumas = 0
for pato in patociudadanos:
    plumas += pato.irse_a_casa()

print(f"En total habian {plumas} plumas")
