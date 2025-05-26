from enum import Enum
from datetime import datetime
import random
import string


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


class Combustion:
    def __str__(self):
        # return f"C<{super().__str__()}>"
        return f"C<{self.tamanyo} -- {self.matricula}>"


class Electrico:
    def __str__(self):
        # return f"E<{super().__str__()}>"
        return f"E<{self.tamanyo} -- {self.matricula}>"


class Vehiculo:

    def __init__(self):
        self.tamanyo = random.choice(list(Tamanyo))
        self.matricula = self.generar_matricula()
        self.entrada = datetime.now()
        self.plaza = None

    def __str__(self):
        entrada = '{:%Y/%m/%d %H:%M:%S}'.format(self.entrada)
        return f"{self.tamanyo} -- {self.matricula} -- {entrada}"

    def generar_matricula(self):
        # Generar 4 dígitos
        numeros = f"{random.randint(0, 9999):04d}"
        # Generar 3 letras mayúsculas excluyendo vocales y algunas letras problemáticas (como Ñ)
        letras_disponibles = ''.join([c for c in string.ascii_uppercase if c not in 'AEIOUÑQ'])
        letras = ''.join(random.choices(letras_disponibles, k=3))

        return f"{numeros} {letras}"


class VehiculoCombustion(Combustion, Vehiculo):
    pass


class VehiculoElectrico(Electrico, Vehiculo):
    pass
