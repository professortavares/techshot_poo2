
from techshot.servicos.servico_informacaopessoal import ServicoInformacaoPessoal
from techshot.servicos.usuario import ServicoUsuario
from techshot.entidades import UsuarioCriacao
from techshot.orm.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from techshot.entidades import InformacaoPessoalCriacao
from techshot.aux_function import codifica_senha
from datetime import datetime, timedelta
from pytest import fixture

@fixture(scope='module')
def session():
    # cria uma instância de engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    # cria as tabelas necessárias
    Base.metadata.create_all(bind=engine)

    # cria uma instância de sessionmaker
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    # cria uma instância de sessão
    session = Session()
    return session

def test_crud_informacao_pessoal(session):
    """
    Testa o CRUD de informação pessoal
    :param session: Sessão do banco de dados
    :return:
    """

    # cria uma data que representa 15 anos atrás
    data_teste =  datetime.now() - timedelta(days=365 * 15)

    # SETUP

    # é necessária a criação de um usuário para que a informação pessoal seja
    # associada a ele
    # cria um novo usuário
    servico = ServicoUsuario(session)
    usuario = servico.criar_usuario(
            UsuarioCriacao(nome='Fulano', nome_usuario='fulano')
        )

    # cria uma nova informação pessoal
    servico = ServicoInformacaoPessoal(session)
    info = InformacaoPessoalCriacao(
        email='a@a.com.br',
        telefone='(11) 99999-9999',
        data_nascimento=data_teste,
        senha='123456')
    # associa a informação pessoal ao usuário
    info = servico.criar_informacao_pessoal(info)
    usuario.informacao_pessoal = info
    session.commit()
    # asserts
    assert info.email == 'a@a.com.br'
    assert info.telefone == '(11) 99999-9999'
    assert info.data_nascimento == data_teste.date()
    assert info.senha == codifica_senha('123456')


    # TESTE
    info = servico.buscar_informacao_pessoal_por_usuario(usuario)
    # asserts
    # asserts
    assert info.email == 'a@a.com.br'
    assert info.telefone == '(11) 99999-9999'
    assert info.data_nascimento == data_teste.date()
    assert info.senha == codifica_senha('123456')


    # alteração da informação pessoal
    info.email = 'b@b.com.br'
    info.telefone = '(11) 88888-8888'
    info.senha = codifica_senha('654321')
    info = servico.atualizar_informacao_pessoal(info)

    # asserts
    assert info.email == 'b@b.com.br'
    assert info.telefone == '(11) 88888-8888'
    assert info.data_nascimento == data_teste.date()
    assert info.senha == codifica_senha('654321')


    # remoção da informação pessoal
    servico.deletar_informacao_pessoal(info)
    # asserts
    assert servico.buscar_informacao_pessoal_por_usuario(usuario) is None
