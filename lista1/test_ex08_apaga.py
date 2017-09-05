# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  s = list(s)
  del s[n]
  return ''.join(s)

def test_ex08():
  print ('Apaga')
  assert apaga('kitten', 1) == 'ktten'
  assert apaga('kitten', 0) == 'itten' 
  assert apaga('kitten', 4) == 'kittn'
  assert apaga('Hi', 0) == 'i'
  assert apaga('Hi', 1) == 'H'
  assert apaga('code', 0) == 'ode'
  assert apaga('code', 1) == 'cde'
  assert apaga('code', 2) == 'coe'
  assert apaga('code', 3) == 'cod'
  assert apaga('chocolate', 8) == 'chocolat'

