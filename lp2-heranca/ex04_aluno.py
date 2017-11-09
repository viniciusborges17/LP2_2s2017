class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
    def estudar(self, tempo):
        self.tempoSemDormir += tempo 
    def dormir(self, tempo):
        self.tempoSemDormir -= tempo