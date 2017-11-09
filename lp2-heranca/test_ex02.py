from ex02_funcionario import Funcionario
funcionario = Funcionario('vitor', 10000)

def test_ex02():
    assert funcionario.aumentarSalario(10) == 11000
    funcionario.salario = 10000
    assert funcionario.aumentarSalario(50) == 15000
    funcionario.salario = 10000
    assert funcionario.aumentarSalario(10.5) == 11050
    funcionario.salario = 10000
    assert funcionario.aumentarSalario(0.7) == 10070