from entregas_tarefa import verifica_prazo

def testprazo():
  print ('Prazo!!')
  assert verifica_prazo(29, 11) == True
  assert verifica_prazo(30, 11) == True
  assert verifica_prazo(25, 10) == False