from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from techshot.entidades import UsuarioCriacao
from techshot.servicos import ServicoUsuario
from techshot.orm.base import Base
from techshot.orm.usuario import Usuario
from techshot.orm.informacao_pessoal import InformacaoPessoal

if __name__ == '__main__':
    # cria uma instância de engine
    engine = create_engine('sqlite:///techshot.db', echo=True)
    # cria as tabelas necessárias
    Base.metadata.create_all(bind=engine)

    # cria uma instância de sessionmaker
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    # cria uma instância de sessão
    session = Session()
    ########
    # CRUD #
    ########
    # cria um novo usuário
    servico = ServicoUsuario(session)
    usuario = servico.criar_usuario(
            UsuarioCriacao(nome='Fulano', nome_usuario='fulano')
        )
    # imprime o usuário criado
    print(usuario)

    # busca o usuário criado
    usuario = servico.buscar_usuario_por_nome_usuario('fulano')
    # imprime o usuário buscado
    print(usuario)

    # Altera o nome do usuário
    usuario.nome = 'Fulano da Silva'
    usuario = servico.atualizar_usuario(usuario)
    print(usuario)

    # deleta o usuário
    servico.deletar_usuario(usuario)
    # busca o usuário deletado
    usuario = servico.buscar_usuario_por_nome_usuario('fulano')
    # imprime o usuário buscado
    print(usuario)



