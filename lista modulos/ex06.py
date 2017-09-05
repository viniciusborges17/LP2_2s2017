def middle_way(a, b):
    lista=[]
    lista.append(a[int(len(a)/2)]) #se você dividir um inteiro ímpar por dois e forçar o resultado para um int, 
    lista.append(b[int(len(b)/2)]) #ele arredonda para baixo! Ex: 3/2 -> 1.5; int(3/2) -> 1
    return lista