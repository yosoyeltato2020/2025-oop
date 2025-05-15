# Definimos la clase Platano
class Platano:
    # el metodo __init__() se llama cuando se crea la instancia
    # Cuando creamos un Platano...

    def __init__(self):
        self.cantidad = 5
        # quitame dinero en la BBDD
        print("Te ha costado 1€")

    # La clase tienen un metodo: comer()
    def comer(self, tamanyo_bocado):
        if self.cantidad <= 0:
            print("no queda")
            return

        self.cantidad -= tamanyo_bocado
        print("Ñan ñam que rico el platano")


# en la variable platano guardamos una instancia(objeto) de clase Platano
platano = Platano()

# Creamos una variable llamada fruta.
# fruta contiene una instancia(objeto) de clase Platano
fruta = Platano()
# Ahora podemos comer() el platano
fruta.comer()
for _ in range(100):
    fruta = Platano()
    fruta.comer()

fruta.comer()
fruta.comer()
fruta.comer()

juguete = Platano()
juguete.comer()
