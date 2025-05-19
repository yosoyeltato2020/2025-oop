from enum import Enum
from datetime import datetime
import random
import string


class Tamanyo(Enum):
    MOTO = 0
    TURISMO = 1
    FURGO = 2

    def __str__(self):
        return ["Moto", "Turi", "Furg"][self.value]


class Vehiculo:
    def __init__(self):
        self.tamanyo = random.choice(list(Tamanyo))
        self.matricula = self.generar_matricula()
        self.entrada = datetime.now()

    def generar_matricula(self):
        numeros = f"{random.randint(0, 9999):04d}"
        letras_disponibles = ''.join([c for c in string.ascii_uppercase if c not in 'AEIOUÑQ'])
        letras = ''.join(random.choices(letras_disponibles, k=3))
        return f"{numeros} {letras}"

    def __str__(self):
        entrada = '{:%Y/%m/%d %H:%M:%S}'.format(self.entrada)
        return f"{self.tamanyo} -- {self.matricula} -- {entrada}"


class Combustion(Vehiculo):
    def __str__(self):
        return f"C<{super().__str__()}>"


class Electrico(Vehiculo):
    def __str__(self):
        return f"E<{super().__str__()}>"


class Plaza:
    def __init__(self, numero):
        self.numero = numero
        self.tamanyo = random.choice(list(Tamanyo))
        self.vehiculo = None

    def ocupar(self, vehiculo):
        if self.vehiculo is None and vehiculo.tamanyo == self.tamanyo:
            self.vehiculo = vehiculo
            return f"Plaza {self.numero} ocupada por {self.vehiculo}"
        elif self.vehiculo is not None:
            return f"Error: La plaza {self.numero} ya está ocupada"
        else:
            return f"Error: El vehículo {vehiculo.matricula} no puede aparcar en la plaza {self.numero}"

    def liberar(self):
        if self.vehiculo is not None:
            vehiculo = self.vehiculo
            self.vehiculo = None
            return f"Plaza {self.numero} liberada de {vehiculo}"
        else:
            return f"Error: La plaza {self.numero} ya está vacía"

    def __str__(self):
        estado = f"Ocupada por {self.vehiculo}" if self.vehiculo else "Vacía"
        return f"Plaza {self.numero} ({self.tamanyo}): {estado}"


class Parking:
    def __init__(self, num_plazas):
        self.plazas = [Plaza(num) for num in range(num_plazas)]

    def asignar_vehiculos(self, vehiculos):
        for plaza in self.plazas:
            for vehiculo in vehiculos:
                if vehiculo.tamanyo == plaza.tamanyo and plaza.vehiculo is None:
                    print(plaza.ocupar(vehiculo))
                    break

    def liberar_plazas(self):
        for plaza in self.plazas:
            if plaza.vehiculo:
                print(plaza.liberar())

    def estado_parking(self):
        for plaza in self.plazas:
            print(plaza)


def demo():
    vehiculos = [random.choice([Combustion, Electrico])() for _ in range(10)]
    parking = Parking(10)

    print("\n--- Asignación de vehículos ---")
    parking.asignar_vehiculos(vehiculos)

    print("\n--- Estado del parking ---")
    parking.estado_parking()

    print("\n--- Liberando plazas ---")
    parking.liberar_plazas()

    print("\n--- Estado final del parking ---")
    parking.estado_parking()


if __name__ == "__main__":
    demo()
