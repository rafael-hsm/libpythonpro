import pytest

from libpythonpro.tests.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'rafameireles2011@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'valhallarhsm@gmail.com',
        'Cursos Python Pro',
        'Turma Iuri Silvio em andamento'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'rafameireles2011']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'valhallarhsm@gmail.com',
            'Cursos Python Pro',
            'Turma Iuri Silvio em andamento'
        )
