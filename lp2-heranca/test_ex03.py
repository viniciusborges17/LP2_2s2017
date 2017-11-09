from ex03_livro import Livro

livro = Livro('Harry Potter', 500, 'J.K.R.', 40.0)
def test_ex_03():
    assert livro.getPreco() == 40.0
    assert livro.setPreco(45.5) == 45.5