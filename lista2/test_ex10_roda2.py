# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# roda2('Hello') -> 'lloHe'
# roda2('Hi') -> 'Hi'
def roda2(s):
  s = list(s)
  lista =[]
  i=2
  while i < len(s):
    lista.append(s[i])
    i += 1
  lista.append(s[0])
  lista.append(s[1])

  return ''.join(lista)

def test_ex10():
  print ('Roda 2')
  assert roda2('Hello') == 'lloHe'
  assert roda2('python') == 'thonpy'
  assert roda2('Hi') == 'Hi'
  assert roda2('code') == 'deco'
  assert roda2('cat') == 'tca'
  assert roda2('12345'), '34512'
  assert roda2('Chocolate') == 'ocolateCh'
  assert roda2('bricks') == 'icksbr'


