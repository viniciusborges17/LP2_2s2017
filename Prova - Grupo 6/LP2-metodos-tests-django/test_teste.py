from aplicacao_teste import verifica_teste

def testteste():
  print ('Teste')
  assert verifica_teste('Tecweb', ['Tecweb', 'Banco de dados', 'Linguagem de Programação']) == False
  assert verifica_teste('Banco de dados', ['Tecweb', 'Linguagem de programação']) == True
  assert verifica_teste('Devops', ['Devops', 'Banco de dados']) == False