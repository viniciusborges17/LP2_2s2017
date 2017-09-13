from ex03 import media_aluno

def test_ex03():
    print('media')
    assert media_aluno("Vitor", {"Thiago": [8, 8], "Bruna": [9, 8], "Vitor":[10, 9]}) == 9.5
    assert media_aluno("Ciclano", {"Fulano": [2, 5], "Ciclano": [5, 7], "Deltrnao": [0 , 1]}) == 6
    assert media_aluno("John", {"Paul": [3, 5], "Ringo": [5, 5], "John": [6, 7], "George": [10, 9]})