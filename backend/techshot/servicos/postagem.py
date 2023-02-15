from techshot.orm.postagem import Postagem
from techshot.orm.usuario import Usuario
from techshot.entidades import PostagemCriacao

class ServicoPostagem:
    """
    Classe de serviço de postagem
    """

    def __init__(self, session):
        """
        Construtor da classe

        Parâmetros:
        -----------
        session: session
            Sessão do banco de dados.
        """
        self.__session = session

    def criar_postagem(self, postagem:PostagemCriacao, nome_usuario:str):
        """
        Método que cria uma nova postagem e
        salva-a no banco de dados.

        Parâmetros:
        -----------
        postagem: Postagem
            Postagem a ser criada.
        nome_usuario: str
            Nome de usuário do usuário que criou a postagem.

        Retorno:
        --------
        Postagem
            Postagem criada.
        """
        # obtém o usuário que criou a postagem
        usuario = self.__session.query(Usuario).filter_by(
            nome_usuario=nome_usuario).first()
        # cria uma instância de postagem
        postagem = Postagem(**postagem.dict(), usuario=usuario)
        # salva a postagem no banco de dados
        self.__session.add(postagem)
        # salva as alterações no banco de dados
        self.__session.commit()
        # retorna a postagem criada
        self.__session.refresh(postagem)

        return postagem

    def buscar_todas_postagem(self)->list:
        """
        Método que obtém todas as postagens do banco de dados.

        Retorno:
        --------
        list
            Lista de postagens.
        """
        return self.__session.query(Postagem).all()

    def buscar_postagem_por_nome_usuario(self, nome_usuario:str)->list:
        """
        Método que obtém todas as postagens de um usuário
        a partir do nome de usuário.

        Parâmetros:
        -----------
        nome_usuario: str
            Nome de usuário do usuário.

        Retorno:
        --------
        list
            Lista de postagens.
        """

        usuario = self.__session.query(Usuario).filter_by(
            nome_usuario=nome_usuario).first()
        if usuario is None:
            raise Exception('Usuário não encontrado.')


        return self.__session.query(Postagem).filter_by(
            usuario=usuario).all()

    def alterar_postagem(self, postagem:Postagem):
        """
        Método que altera uma postagem.

        Parâmetros:
        -----------
        postagem: Postagem
            Postagem a ser alterada.
        """
        # obtém a postagem a ser alterada
        postagem_bd = self.__session.query(Postagem).filter_by(
            id=postagem.id).first()
        # altera os dados da postagem
        postagem_bd.titulo = postagem.titulo
        postagem_bd.texto = postagem.texto
        # salva as alterações no banco de dados
        self.__session.commit()

    def excluir_postagem(self, id:int):
        """
        Método que exclui uma postagem.

        Parâmetros:
        -----------
        id: int
            Id da postagem a ser excluída.
        """
        # obtém a postagem a ser excluída
        postagem = self.__session.query(Postagem).filter_by(id=id).first()
        # exclui a postagem
        self.__session.delete(postagem)
        # salva as alterações no banco de dados
        self.__session.commit()