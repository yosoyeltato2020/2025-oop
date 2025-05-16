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


if __name__ == "__main__":
    caosZoologico()
