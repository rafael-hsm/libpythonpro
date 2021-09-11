from libpythonpro.spam.modelos import Usuario


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
