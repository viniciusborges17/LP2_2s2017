# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  
def extra_end(s):
  s=list(s)
  lista =[]
  for i in range(0, 3):
    lista.append(s[len(s)-2])
    lista.append(s[len(s)-1])

  return ''.join(lista)

def test_ex07():
  print ('Extra End')
  assert extra_end('Hello') == 'lololo'
  assert extra_end('ab') == 'ababab'
  assert extra_end('Hi') == 'HiHiHi'
  assert extra_end('Candy') == 'dydydy'
  assert extra_end('Code') == 'dedede'

