def verifica_matricula(disciplina, disciplinas_matriculadas):
    if disciplina in disciplinas_matriculadas:
        return False
    else:
        return True