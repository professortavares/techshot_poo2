from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from techshot.orm.base import Base

class InformacaoPessoal(Base):
    """
    Classe que representa as informações pessoais
    de um usuário da rede social Piui, mapeado
    para o banco de dados.
    """
    __tablename__ = 'tb_informacao_pessoal'
    # Coluna que representa o id da informação pessoal.
    id = Column(Integer, primary_key=True)
    # Coluna que representa a data em que o objeto foi criado.
    data_criacao = Column(DateTime, nullable=False)
    # Coluna que representa a data em que o objeto foi atualizado.
    data_atualizacao = Column(DateTime, nullable=False)
    # Coluna que representa a versao em que o objeto se encontra.
    versao = Column(Integer, nullable=False, autoincrement=True)

    # Coluna que representa o email do usuário.
    email = Column(String(255), nullable=False, unique=True)
    # Coluna que representa o telefone do usuário.
    telefone = Column(String(50), nullable=False)
    # Coluna que representa a senha do usuário.
    senha = Column(String(255), nullable=False)
    # Coluna que representa a data de nascimento do usuário.
    data_nascimento = Column(Date, nullable=False)

    # Coluna que representa o id do usuário.
    id_usuario = Column(Integer, ForeignKey('tb_usuario.id'))
    # Coluna que representa o relacionamento com a tabela de usuários.
    usuario = relationship('Usuario', back_populates='informacao_pessoal')


    def __repr__(self):
        return f'InformacaoPessoal(id={self.id}, email={self.email}, telefone={self.telefone})'