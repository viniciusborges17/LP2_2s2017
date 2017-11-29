from calculo_media import calcular_media

def testmedia():
  print ('Média!!')
  assert calcular_media([1, 2, 6]) == 3
  assert calcular_media([6, 1, 2, 3]) == 3
  assert calcular_media([3, 2, 1]) == 2
  