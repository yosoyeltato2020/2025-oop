from parroquiano import Parroquiano


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
