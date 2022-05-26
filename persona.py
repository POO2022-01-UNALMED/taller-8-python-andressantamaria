class Persona:
    def __init__(self, name, age, height, sex):
        self._nombre = name
        self._edad = age
        self._altura = height
        self._sexo = sex

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getAltura(self):
        return self._altura

    def getSexo(self):
        return self._sexo

    def setNombre(self, nn):
        self._nombre = nn

    def setEdad(self, ee):
        self._edad = ee

    def setEdad(self, aa):
        self._edad = aa

    def setSexo(self, ss):
        self._sexo = ss
