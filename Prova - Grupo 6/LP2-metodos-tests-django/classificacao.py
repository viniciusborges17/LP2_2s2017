def classificacao(historico):
    media = 0
    for nota in historico:
        media += nota
    media = media/len(historico)
    if media >= 7:
        return "bom"
    elif 7 > media >=5:
        return "regular"
    else:
        return "fraco"