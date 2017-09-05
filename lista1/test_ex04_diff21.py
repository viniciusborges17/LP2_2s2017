# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# D. diff21
# dado um inteiro n retorna a diferença absoluta entre n e 21
# porém se o número for maior que 21 retorna dobro da diferença absoluta
# diff21(19) -> 2
# diff21(25) -> 8
# dica: abs(x) retorna o valor absoluto de x
def diff21(n):
  if n<=21:
    return abs(n-21)
  else:
    return abs(n-21)*2 


def test_ex04():
  print ('Diff21')
  assert diff21(19) == 2
  assert diff21(10) == 11
  assert diff21(21) == 0
  assert diff21(22) == 2
  assert diff21(25) == 8
  assert diff21(30) == 18


