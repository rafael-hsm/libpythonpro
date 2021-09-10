from libpythonpro.tests.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'rafameireles2011@gmail.com',
        'valhallarhsm@gmail.com',
        'Cursos Python Pro',
        'Turma Iuri Silvio em andamento'
    )
    assert 'rafameireles2011@gmail.com' in resultado