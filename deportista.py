class Deportista:
    def __init__(self, years):
        self._deporte = "Futbol"
        self._añosPracticando = years

    def getDeporte(self):
        return self._deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setDeporte(self, dd):
        self._deporte = dd

    def setAñosPracticando(self, apap):
        self._añosPracticando = apap
