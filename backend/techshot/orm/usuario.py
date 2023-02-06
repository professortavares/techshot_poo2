from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from techshot.orm.base import Base


class Usuario(Base):
    """
    Classe que representa um usuário da rede
    social Piui, mapeado para o banco de dados.
    """

    # Nome da tabela no banco de dados.
    __tablename__ = 'tb_usuario'

    # Coluna que representa o id do usuário.
    id = Column(Integer, primary_key=True)
    # Coluna que representa a data em que o objeto foi criado.
    data_criacao = Column(DateTime, nullable=False)
    # Coluna que representa a data em que o objeto foi atualizado.
    data_atualizacao = Column(DateTime, nullable=False)
    # Coluna que representa a versao em que o objeto se encontra.
    versao = Column(Integer, nullable=False, autoincrement=True)

    # Coluna que representa o nome do usuário.
    nome = Column(String(50), nullable=False)
    # Coluna que representa o nome de usuário (@).
    nome_usuario = Column(String(50), nullable=False, unique=True)

    # Relacionamento com a tabela de postagens.
    postagens = relationship('Postagem', back_populates='usuario')
    # Relacionamento com a tabela de informações pessoais.
    informacao_pessoal = relationship('InformacaoPessoal', back_populates='usuario')

    def __repr__(self):
        return f'Usuario(id={self.id}, nome={self.nome}, nome_usuario={self.nome_usuario})'
