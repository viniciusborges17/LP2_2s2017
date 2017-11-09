class Livro:
    def __init__(self, nome, paginas, autor, preco):
        self.nome = nome
        self.paginas = paginas
        self.autor = autor
        self.preco = preco
    def getPreco(self):
        return self.preco
    def setPreco(self, valor):
        self.preco = valor
        return self.preco