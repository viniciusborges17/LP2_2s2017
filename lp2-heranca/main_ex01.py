from ex01_triangulo import Triangulo

ladoA = int(input('Digite o primeiro lado:\n'))
ladoB = int(input("Digite o segundo lado:\n"))
ladoC = int(input("Digite o terceiro lado:\n"))

triangulo = Triangulo(ladoA, ladoB, ladoC)
print(triangulo.perimetro())
print(triangulo.getMaior())