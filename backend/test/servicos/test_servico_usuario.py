from techshot.servicos import ServicoUsuario
from techshot.orm.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from techshot.entidades import UsuarioCriacao
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

def testar_crud_usuario(session):
    # cria um novo usuário
    servico = ServicoUsuario(session)
    _ = servico.criar_usuario(
            UsuarioCriacao(nome='Fulano', nome_usuario='fulano')
        )
    # busca o usuário criado
    usuario = servico.buscar_usuario_por_nome_usuario('fulano')
    # imprime o usuário buscado
    assert usuario.nome == 'Fulano'
    assert usuario.nome_usuario == 'fulano'

    # Altera o nome do usuário
    usuario.nome = 'Fulano da Silva'
    _ = servico.atualizar_usuario(usuario)
    usuario = servico.buscar_usuario_por_nome_usuario('fulano')
    assert usuario.nome == 'Fulano da Silva'

    # deleta o usuário
    servico.deletar_usuario(usuario)
    # busca o usuário deletado
    usuario = servico.buscar_usuario_por_nome_usuario('fulano')
    # verifica que o usuário foi deletado
    assert usuario is None

def testar_criar_usuario(session):
    # cria um novo usuário
    servico = ServicoUsuario(session)
    _ = servico.criar_usuario(
            UsuarioCriacao(nome='Outro Fulano', nome_usuario='fulano2')
        )
    # busca o usuário criado
    usuario = servico.buscar_usuario_por_nome_usuario('fulano2')
    assert usuario.nome == 'Outro Fulano'
    assert usuario.nome_usuario == 'fulano2'

