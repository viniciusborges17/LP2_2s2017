class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC 
    def getMaior(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            return self.ladoA
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            return self.ladoB
        else:
            return self.ladoC
