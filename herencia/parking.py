import random
from vehiculo import *


class Plaza:
    def __init__(self, numero):
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
