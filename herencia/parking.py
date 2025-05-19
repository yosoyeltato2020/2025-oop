from enum import Enum
from datetime import datetime
import random
import string


# class syntax
class Tamanyo(Enum):
    MOTO = 0
    TURISMO = 1
    FURGO = 2

    def __str__(self):
        if self.value == 0:
            return "Moto"
        elif self.value == 1:
            return "Turi"
        elif self.value == 2:
            return "Furg"
        else:
            return "UNDEFINED"


class Vehiculo:
    def __init__(self):
        self.tamanyo = random.choice(list(Tamanyo))
        self.matricula = self.generar_matricula()
        self.entrada = datetime.now()

    def generar_matricula(self):
        # Generar 4 dígitos
        numeros = f"{random.randint(0, 9999):04d}"
        # Generar 3 letras mayúsculas excluyendo vocales y algunas letras problemáticas (como Ñ)
        letras_disponibles = ''.join([c for c in string.ascii_uppercase if c not in 'AEIOUÑQ'])
        letras = ''.join(random.choices(letras_disponibles, k=3))

        return f"{numeros} {letras}"

    def __str__(self):
        entrada = '{:%Y/%m/%d %H:%M:%S}'.format(self.entrada)
        return f"{self.tamanyo} -- {self.matricula} -- {entrada}"


for i in range(10):
    print(Vehiculo())


"""
class Plaza:
    numero
    tamaño ["moto", "turismo", "furgo"]
    vehiculo Vehiculo
"""