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
