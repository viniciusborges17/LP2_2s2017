# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# I. troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  if len(s) > 1:
    s = list(s)
    s_1 = s[0]
    s[0] = s[len(s)-1]
    s[len(s)-1] = s_1
    return ''.join(s)
  else:
    return s

def test_ex09():
  print ('Troca letras')
  assert troca('code') == 'eodc'
  assert troca('a') == 'a'
  assert troca('ab') == 'ba'
  assert troca('abc') == 'cba'
  assert troca('') == ''
  assert troca('Chocolate') == 'ehocolatC'
  assert troca('nythoP') == 'Python'
  assert troca('hello') == 'oellh'


