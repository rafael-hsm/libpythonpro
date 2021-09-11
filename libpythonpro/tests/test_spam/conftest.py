import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
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