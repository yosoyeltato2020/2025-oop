import random

import string


class Tamanyo(Enum):
    MOTO = 0
    TURISMO = 1
    FURGO = 2
    VMR = 3

    def __str__(self):
        if self.value == 0:
            return "Moto"
        elif self.value == 1:
            return "Turi"
        elif self.value == 2:
            return "Furg"
        elif self.value ==3:
            return "VMR"
        else:
            return "UNDEFINED"


class Vehiculo:

    def __init__(self):
        self.tamanyo = random.choice(list(Tamanyo))
        self.matricula = self.generar_matricula()
        self.entrada = datetime.now()

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


class Combustion(Vehiculo):
    def __str__(self):
        return f"C<{super().__str__()}>"


class Electrico(Vehiculo):
    def __str__(self):
        return f"E<{super().__str__()}>"

from vehiculo import *


class Hibrido(Vehiculo):
    def __str__(self):
        return f"H<{super().__str__()}>"
    
class Plaza:
    def __init__(self, numero, tamanyo=None):
        self.numero = numero
        self.tamanyo = random.choice(list(Tamanyo))
        self.vehiculo = None 

    def ocupar(self, vehiculo):
        if vehiculo.tamanyo == self.tamanyo:
            self.vehiculo = vehiculo
            self.vehiculo.plaza = self

            return f"{self.numero} ocupado por {self.vehiculo}"

    def liberar(self):
        self.vehiculo.plaza = None
        vehiculo = self.vehiculo
        self.vehiculo = None

        return f"{self.numero} liberado de {vehiculo}"


class Parking:
    def demo(self):
        def generarVehiculos():
            vehiculos = []
            for _ in range(5):
                vehiculos.append(VehiculoCombustion())
                vehiculos.append(VehiculoElectrico())
            return vehiculos


    vehiculos = []
    for _ in range(5):
        vehiculos.append(Combustion())
        vehiculos.append(Electrico())
        vehiculos.append(Hibrido())

    plazas = []
    for num in range(10):
        if num < 2:
           plazas.append(Plaza(num, Tamanyo.VMR))
        else:
            plazas.append(Plaza(num))

        def generarPlazas():
            plazas = []
            for num in range(10):
                plazas.append(Plaza(num))
            return plazas

        def rellenar(plazas, vehiculos):
            for plaza in plazas:
                for vehiculo in vehiculos:
                    if vehiculo.plaza is None and vehiculo.tamanyo == plaza.tamanyo:
                        print(plaza.ocupar(vehiculo))
                        break


        def vaciar(plazas):
            for plaza in plazas:
                if isinstance(plaza.vehiculo, Vehiculo):
                    print(plaza.liberar())

        vehiculos = generarVehiculos()
        plazas = generarPlazas()
        rellenar(plazas, vehiculos)
        vaciar(plazas)


if __name__ == "__main__":
    parking = Parking()
    parking.demo()
