from confere_matricula import verifica_matricula

def testmatricula():
  print ('Matricula!!')
  assert verifica_matricula('Tecweb', ['Tecweb', 'Banco de dados', 'Linguagem de Programação']) == False
  assert verifica_matricula('Banco de dados', ['Tecweb', 'Linguagem de programação']) == True
  assert verifica_matricula('Devops', ['Devops', 'Banco de dados']) == False