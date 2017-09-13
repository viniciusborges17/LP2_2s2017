def calcula_mdc(a,b):
    if a >= b:
        resto = a%b
        while resto != 0:
            a = b
            b = resto
            resto = a%b
        return b
    else:
        resto = b%a
        while resto != 0:
            b = a
            a = resto
            resto = b%a
        return a


#a = int(input("Digite o primeiro valor: "))
#b = int(input("Digite o segundo valor: "))
#print(calcula_mdc(a,b))