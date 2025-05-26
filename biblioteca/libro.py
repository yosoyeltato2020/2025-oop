class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        self.socio = None

    def info(self) -> str:
        txt = f"Libro: {self.titulo} por {self.autor}"
        if self.prestado:
            txt += f" prestado a {self.socio}"

        return txt

    def prestar(self, socio: Socio) -> bool:
        if not self.prestado:
            self.prestado = True
            self.socio = socio
            return True

        return False

    def leer(self):
        pass
