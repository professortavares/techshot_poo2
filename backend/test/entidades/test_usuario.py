import pytest
from datetime import datetime, timedelta
from techshot.entidades import UsuarioCriacao
from techshot.entidades import InformacaoPessoalCriacao

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
    usuario = UsuarioCriacao(nome='Fulano de Tal',
                      nome_usuario='@fulano')

    # execução
    # é a execução do método em si que será testado

    # asserts
    # são as verificações que serão feitas
    # para validar se o método está funcionando
    assert usuario.nome == 'Fulano de Tal'
    assert usuario.nome_usuario == '@fulano'

def testar_usuario_tamanho_nome():
    """
    Método responsável por testar a criação
    de um usuário com um nome que não corresponde
    as regras do requisito.

    Cenário de teste: o usuário possui um nome
    com menos de 3 caracteres.
    """
    # setup
    # prepara os objetos para serem testados

    with pytest.raises(ValueError):
        UsuarioCriacao(nome='Jo',
                nome_usuario='@fulano')

def testar_usuario_tamanho_senha():
    """
    Método responsável por testar a criação
    de um usuário com uma senha que não corresponde
    as regras do requisito.

    Cenário de teste: o usuário possui uma senha
    com menos de 6 caracteres.
    """
    # setup
    # prepara os objetos para serem testados

    with pytest.raises(ValueError):
        InformacaoPessoalCriacao(
            email='a@a.com.br',
            telefone='(11) 99999-9999',
            senha='12345',
            data_nascimento=datetime(1990, 1, 1)
        )

def testar_usuario_idade():
    """
    Método responsável por testar a criação
    de um usuário com uma senha que não corresponde
    as regras do requisito.

    Cenário de teste: o usuário tem menos de 12 anos de idade.
    """
    # setup
    # prepara os objetos para serem testados

    with pytest.raises(ValueError):
        InformacaoPessoalCriacao(
            email='a@a.com.br',
            telefone='(11) 99999-9999',
            senha='123457',
            data_nascimento=datetime.now()-timedelta(days=3660)
        )