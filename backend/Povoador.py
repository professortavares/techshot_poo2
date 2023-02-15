from techshot.servicos.usuario import ServicoUsuario
from techshot.entidades import UsuarioCriacao
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from techshot.orm.base import Base

if __name__ == "__main__":
    print("Hello World")

    # cria uma instância de engine
    engine = create_engine('sqlite:///./volume/techshot.db', echo=True)
    # cria as tabelas necessárias
    Base.metadata.create_all(bind=engine)

    # cria uma instância de sessionmaker
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    # cria uma instância de sessão
    session = Session()

    servico = ServicoUsuario(session)

    # Cria 10 usuários
    for i in range(10):
        usuario = UsuarioCriacao(nome=f'Fulano {i}', nome_usuario=f'fulano{i}')
        servico.criar_usuario(usuario)