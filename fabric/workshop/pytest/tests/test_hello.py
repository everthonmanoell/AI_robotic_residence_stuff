import pytest
from workshop_pytest.hello import hello_world

# def test_hello_world_retorna_hello_world():
#     retorno = hello_world()
#     assert "Hello, Wordl!" == retorno



@pytest.mark.marcado
def test_marcado():
    assert 1 == 1
    
@pytest.mark.skip(reason="Ainda não implementado")
def test_para_pular():
    text = 'algo'
    assert 'a' in text

@pytest.mark.skipif(True, reason="Condição para pular o teste")
def test_para_pular_com_condicao():
    ...

@pytest.mark.xfail(reason="Teste que deve falhar")
def test_para_falhar():
    ...

# @pytest.mark.parametrize("entrada, esperado", [
#     (1, 2),
#     (2, 3),
#     (3, 4),])
def test_varias_entradas():
    ...

