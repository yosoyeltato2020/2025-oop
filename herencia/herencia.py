# from animales import Perro, Larva, Gremlin
from animales import *


def caosZoologico():
    firulais = Perro("Firulais", "ChowChow")
    firulais.come()
    firulais.pasea()

    mizgo = Larva("Mizgo")
    mizgo.come()

    gizmo = Gremlin("Gizmo")
    gizmo.come()

    firulais.registrar()
    gizmo.registrar()

    bucefalo = Caballo("bucefalo")
    bucefalo.come()
    bucefalo.registrar()
    bucefalo.carga(150)


if __name__ == "__main__":
    caosZoologico()
