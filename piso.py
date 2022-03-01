class Piso:
    def __init__(self):
        self.nombre = None
        self.patrones = None
        self.R = 0
        self.C = 0
        self.F = 0
        self.S = 0
    
    # METODOS GET
    def getNombre(self):
        return self.nombre

    def getPatrones(self):
        return self.patrones

    def getR(self):
        return self.R
    
    def getC(self):
        return self.C

    def getF(self):
        return self.F
    
    def getS(self):
        return self.S

    # METODOS SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPatrones(self, patrones):
        self.patrones = patrones

    def setR(self, R):
        self.R = R

    def setC(self, C):
        self.C = C
    
    def setF(self, F):
        self.F = F
    
    def setS(self, S):
        self.S = S
