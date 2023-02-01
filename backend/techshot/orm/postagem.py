from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from techshot.orm.base import Base
from datetime import datetime
class Postagem(Base):
    """
    Classe que representa uma postagem na rede
    social Piui, mapeado para o banco de dados.
    """

    # Nome da tabela no banco de dados.
    __tablename__ = 'tb_postagem'

    # Coluna que representa o id da informação pessoal.
    id = Column(Integer, primary_key=True)
    # Coluna que representa a data em que o objeto foi criado.
    data_criacao = Column(DateTime, nullable=False, default=datetime.now)
    # Coluna que representa a data em que o objeto foi atualizado.
    data_atualizacao = Column(DateTime, nullable=False, default=datetime.now)
    # Coluna que representa a versao em que o objeto se encontra.
    versao = Column(Integer, nullable=False, autoincrement=True, default=1)

    # Coluna que representa o texto da postagem.
    texto = Column(String(255), nullable=False)
    # Coluna que representa o id do usuário que postou.
    id_usuario = Column(Integer, ForeignKey('tb_usuario.id'))
    # Coluna que representa o relacionamento com a tabela de usuários.
    usuario = relationship('Usuario', back_populates='postagens')