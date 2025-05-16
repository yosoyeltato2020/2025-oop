class Copa:
    def __init__(self):
        self.capacidad = 500
        self.cantidad = 0

    def llenar(self):
        self.cantidad = 1.0

    def vaciar(self, cantidad):
        if cantidad > self.cantidad:
            cantidad = self.cantidad
        self.cantidad -= cantidad


class Parroquiano:
    def __init__(self):
        self.copa = Copa()
        self.dinero = 5

    def pedir(self):
        self.dinero -= 1
        self.copa.llenar()

    def beber(self):
        self.copa.vaciar(0.2)


class Taberna:
    def demo(self):
        barney = Parroquiano()
        while barney.dinero > 0:
            barney.pedir()
            while barney.copa.cantidad > 0:
                barney.beber()


if __name__ == "__main__":
    taberna = Taberna()
    taberna.demo()

    print(taberna)
