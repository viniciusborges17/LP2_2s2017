class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def aumentarSalario(self, valor):
        self.salario += (self.salario * valor) / 100
        return self.salario
