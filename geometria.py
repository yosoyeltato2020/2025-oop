class Rectangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def area(self):
        return self.lado_a * self.lado_b


class Cuadrado(Rectangulo):
    def __init__(self, lado):  # lado = 4
        super().__init__(lado, lado)

    # Si solo estoy heredando, no necesito expresarlo
    # def area(self):
    #     return super().area()


class Cubo(Cuadrado):
    # Es cuando expando comportamientos que necesito referir al previo
    def area(self):
        return super().area() * 6

    def volumen(self):
        area_cara = super().area()
        return area_cara * self.lado


class Cuakilatero(Cuadrado):
    def area(self):
        return 1

    def volumen(self):
        return super().volumen() ** 0.5


class Cuakicubo(Cuakilatero):
    def area(self):
        return super().area() * 6


r = Rectangulo(1, 1)
print(f"Area del Rectangulo {r.area()}")

c = Cuadrado(1)
print(f"Area del Cuadrado {c.area()}")

q = Cubo(1)
print(f"Area del Cubo {q.area()}")
