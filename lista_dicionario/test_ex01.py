from ex01 import calcula_mdc

def test_ex02():
  print ('MDC')
  assert calcula_mdc(7, 49) == 7
  assert calcula_mdc(12, 4) == 4
  assert calcula_mdc(220, 348) == 4
  assert calcula_mdc(35, 140) == 35