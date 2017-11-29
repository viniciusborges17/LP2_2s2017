def limite_turma(turmas, turma_matriculada):
    if turmas[turma_matriculada] < 25:
       return "Sucesso!"
    else:
        return "Esta sala está cheia!"