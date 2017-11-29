def confere_envio(turmas_respostas):
    lista_turma = []
    for aluno in turmas_respostas:
        if turmas_respostas[aluno]:
            lista_turma.append(aluno)
    return lista_turma

def nao_enviaram(turmas_respostas):
    lista_turma = []
    for aluno in turmas_respostas:
        if turmas_respostas[aluno] == False:
            lista_turma.append(aluno)
    return lista_turma