from limite_turma import limite_turma

turmas = {
    'LP-II-A': 25,
    'Tecweb-A': 15,
    'Banco de dados-A': 30,
    'LP-II-B': 20,
    'Tecweb-B': 12,
    'Banco de dados-B': 35
}

def testlimiteTurma():
  print ('Limite turma')
  assert limite_turma(turmas, 'Banco de dados-A') == "Esta sala está cheia!"
  assert limite_turma(turmas, 'Tecweb-A') == "Sucesso!"
  assert limite_turma(turmas, 'Banco de dados-B') == "Esta sala está cheia!"