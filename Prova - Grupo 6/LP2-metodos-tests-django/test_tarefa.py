from enviaram_tarefa import confere_envio, nao_enviaram

turma1 = {
    "Pedro": True,
    "Lucas" : False,

}

turma2 = {
    "Pedro": False,
    "Lucas" : True,

}

def testconfireEnvio():
  print ('Cofere envio')
  assert confere_envio(turma1) == ["Pedro"]
  assert confere_envio(turma2) == ["Lucas"]


def testnaoEnviaram():
  print ('Não enviaram')
  assert nao_enviaram(turma1) == ["Lucas"]
  assert nao_enviaram(turma2) == ["Pedro"]