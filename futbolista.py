from persona import Persona
from deportista import Deportista


class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, name, age, height, sex, years, score, redCard, leg):
        self._golesMarcados = score
        self._tarjetasRojas = redCard
        self._piernaHabil = leg
        Persona.__init__(self, name, age, height, sex)
        Deportista.__init__(self, years)
        Futbolista.listaFutbolistas.append(self)

    def __str__(self):
        return (
            f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()}"
            f" Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
        )

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, score):
        self._golesMarcados = score

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, redCard):
        self._tarjetasRojas = redCard

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, leg):
        self._piernaHabil = leg
