class Copa:
    def __init__(self, capacidad, cantidad):
        self.capacidad = int(capacidad)
        if cantidad > capacidad:
            raise ValueError("La cantidad no puede ser mayor que la capacidad")
        self.cantidad = float(cantidad)

    def llenar(self):
        self.cantidad = float(self.capacidad)

    def vaciar(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"En la copa queda {self.cantidad}")
        else:
            self.cantidad = 0
            print("La copa está vacía")

class Parroquiano:
    def __init__(self, copa, dinero):
        self.copa = copa
        self.dinero = dinero

    def pedir(self):
        if self.dinero >= 1:
            self.copa.llenar()
            self.dinero -= 1
            print("El parroquiano tiene dinero y ha pedido una copa.")
        else:
            print("No tiene suficiente dinero para pedir asi que hasta luego lucas.")

    def beber(self):
        if self.copa.cantidad > 0:
            self.copa.vaciar(0.25)
            print("El parroquiano bebe una parte de la copa.")
        else:
            print("La copa está vacía.")

# Crear objetos y realizar acciones de forma controlada
la_copa = Copa(capacidad=1000, cantidad=1.0)
parroquiano = Parroquiano(copa=la_copa, dinero=5)

# Ahora puedes llamar a los métodos cuando lo desees
parroquiano.pedir()
parroquiano.beber()