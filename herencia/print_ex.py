from random import randint


class Numero():
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        millones = randint(50, 200)
        return f"{self.valor} premiado con {millones} millones de EUROS"


foo = Numero(42)
bar = Numero(42)
boletos = [
    f"Manolo me trajo el numero: [{foo}]",
    f"Marta  me trajo el numero: [{bar}]"
]

for boleto in boletos:
    if "Eusebio" in boleto:
        print(boleto)


print("==========================")
print(boletos)