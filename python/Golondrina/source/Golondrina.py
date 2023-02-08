class Golondrina:
    def __init__(self):
        self._distancia = 0

    def volar(self, kilometros):
        self._distancia += abs(kilometros)

    def distancia(self):
        return self._distancia

