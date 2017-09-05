# -*- coding: utf-8 -*-
# Exercícios by Nick Parlante (CodingBat)

# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
  return abs(n-100) <= 10 or abs(n-200) <= 10


def test_ex07():
  print ('Dista 10')
  assert dista10(93) == True
  assert dista10(90) == True
  assert dista10(89) == False
  assert dista10(110) == True
  assert dista10(111) == False
  assert dista10(121) == False
  assert dista10(0) == False
  assert dista10(5) == False
  assert dista10(191) == True
  assert dista10(189) == False
  assert dista10(190) == True
  assert dista10(200) == True
  assert dista10(210) == True
  assert dista10(211) == False
  assert dista10(290) == False


