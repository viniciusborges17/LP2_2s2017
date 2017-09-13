def conta_vogal(texto):
    vogais={
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    texto = texto.lower()
    vogais['a'] = texto.count('a')
    vogais['e'] = texto.count('e')
    vogais['i'] = texto.count('i')
    vogais['o'] = texto.count('o')
    vogais['u'] = texto.count('u')

    return vogais

print(conta_vogal("Construir estruturas de testes e muito chato!"))