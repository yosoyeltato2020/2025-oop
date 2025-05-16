from copa import Copa


class Parroquiano:
    def __init__(self):
        self.copa = Copa()
        self.dinero = 5

    def pedir(self):
        self.dinero -= 1
        self.copa.llenar()

    def beber(self):
        self.copa.vaciar(0.2)
