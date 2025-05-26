import copy
from biblioteca import Biblioteca
from libro import Libro
from pelicula import Pelicula


def demo():
    a = Biblioteca()
    a.inventario.append(Libro("Manolito gafotas", "Elvira Lindo"))
    a.inventario.append(Pelicula())

    print(f"a.cantidad: {a.cantidad()}")
    for elemento in a.inventario:
        print(elemento.info())


    a.inventario[1].prestar("Marta", 10)


    for elemento in a.inventario:
        if not elemento.prestado:
            elemento.prestar("Paco")

    


    print(Biblioteca())
    print(Pelicula())



if __name__ == "__main__":
    demo()
