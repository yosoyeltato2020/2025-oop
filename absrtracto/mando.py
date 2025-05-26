from abc import ABCMeta, abstractmethod


class Mando(metaclass=ABCMeta):
    @abstractmethod
    def siguiente_canal(self):
        pass
    @abstractmethod
    def canal_anterior(self):
        pass
    @abstractmethod
    def subir_volumen(self):
        pass
    @abstractmethod
    def bajar_volumen(self):
        pass
