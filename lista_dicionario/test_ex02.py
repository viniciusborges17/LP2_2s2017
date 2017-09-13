from ex02 import conta_vogal

def test_ex02():
  print ('conta_vogal')
  assert conta_vogal('Python e muito legal!') == {'a': 1, 'e': 2, 'i': 1, 'o': 2, 'u': 1}
  assert conta_vogal('Linguagem de programacao e legal!') == {'a': 5, 'e': 4, 'i': 1, 'o': 2, 'u': 1}
  assert conta_vogal('Python e uma linguagem interpretada.') == {'a': 4, 'e': 4, 'i': 2, 'o': 1, 'u': 2}
  assert conta_vogal('Construir estruturas de testes e muito chato!') == {'a': 2, 'e': 5, 'i': 2, 'o': 3, 'u': 4}