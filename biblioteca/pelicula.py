from random import randint


class Pelicula:
    def __init__(self):
        self.precio = 10
        self.id = randint(1, 5000)
        self.prestado = False

    def info(self) -> str:
        return f"PELI {self.id}"

    def prestar(self, socio: str) -> bool:
        print(f"Pelicula a {socio}")
        return False

    def reproducir(self):
        pass
