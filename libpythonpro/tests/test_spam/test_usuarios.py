import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield Conexao()
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()  # Serve para desfazer todas as operações feitas durante o teste
    sessao_obj.fechar()


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Rafael')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Rafael'), Usuario(nome='Dexter')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()  # Serve para desfazer todas as operações feitas durante o teste
    sessao.fechar()
    conexao.fechar()
