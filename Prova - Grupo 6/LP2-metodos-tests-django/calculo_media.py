def calcular_media(notas):
    media = 0
    for nota in notas:
        media += nota
    return media/len(notas)
