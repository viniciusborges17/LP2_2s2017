from classificacao import classificacao

def testclassificacao():
  print ('Classificação!!')
  assert classificacao([10, 10, 10]) == 'bom'
  assert classificacao([4, 6, 6, 4]) == 'regular'
  assert classificacao([1, 1, 1, 1]) == 'fraco'