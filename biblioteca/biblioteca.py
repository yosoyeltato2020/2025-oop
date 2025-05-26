class Biblioteca():
    def __init__(self):
        self.inventario = []
        print("La biblioteca ha sido creada")

    def cantidad(self):
        return len(self.inventario)
