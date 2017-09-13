def notas():
    nomes = []
    notas1 = []
    notas2 = []
    alunos = { }

    while 1:
        nome = input("Qual o nome do aluno?")
        if nome == ' ':
            break;
        notas1.append(int(input("Qual a primeira nota?")))
        notas2.append(int(input("Qual a segunda nota?")))
        nomes.append(nome.lower())

    i = 0
    while i < len(nomes):
        alunos[nomes[i]] = [notas1[i], notas2[i]]
        i+=1

    return alunos

def media_aluno(nome, notas):
    for i in notas:
        if i == nome:
            nota = notas[i]
            break;
    media = (nota[0]+nota[1])/2
    return media

# alunos = notas()
# nome = input("Qual o nome do aluno que voce deseja saber a media?")
# print(media_aluno(nome, alunos))