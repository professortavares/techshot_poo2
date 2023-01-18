from datetime import datetime
from techshot.entidades import Usuario
from techshot.entidades import InformacaoPessoal

def test_usuario_sucesso():
    """
    Método responsável por testar a criação
    de um usuário com sucesso.

    Cenário de teste: o usuário possui todas as suas
    informações corretas e prontas para serem
    utilizadas.
    """
    # setup
    # prepara os objetos para serem testados
    usuario = Usuario('Fulano de Tal', '@fulano')
    informacao_pessoal = InformacaoPessoal(
        email='a@a.com.br',
        telefone='(11) 99999-9999',
        senha='123456',
        data_nascimento=datetime(1990, 1, 1)
    )
    usuario.informacoes_pessoais = informacao_pessoal

    # execução
    # é a execução do método em si que será testado

    # asserts
    # são as verificações que serão feitas
    # para validar se o método está funcionando
    assert usuario.nome == 'Fulano de Tal'
    assert usuario.nome_usuario == '@fulano'
    assert usuario.informacoes_pessoais is not None
    assert usuario.informacoes_pessoais.email == 'a@a.com.br'
    assert usuario.informacoes_pessoais.telefone == '(11) 99999-9999'
    assert usuario.informacoes_pessoais.senha == '123456'
    assert usuario.informacoes_pessoais.data_nascimento == datetime(1990, 1, 1)
    assert usuario.postagens == []