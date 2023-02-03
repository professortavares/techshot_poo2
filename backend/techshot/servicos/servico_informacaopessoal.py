from datetime import datetime

from techshot.entidades.informacao_pessoal import InformacaoPessoalCriacao
from techshot.orm.informacao_pessoal import InformacaoPessoal

class ServicoInformacaoPessoal:

    def __init__(self, session):
        """
        Construtor da classe.
        :param session: Sessão do banco de dados.
        """
        self.__session = session

    def criar_usuario(self, dados_usuario:UsuarioCriacao):
        """
        Método que cria um novo usuário e
        salvá-lo no banco de dados.
        :param dados_usuario: Dados do usuário que será criado.
        :return: Usuário criado.
        """

        # cria uma instância de usuário
        usuario = Usuario(**dados_usuario.dict())
        usuario.versao = 1
        usuario.data_criacao = datetime.now()
        usuario.data_atualizacao = datetime.now()


        # salva o usuário no banco de dados
        self.__session.add(usuario)
        # salva as alterações no banco de dados
        self.__session.commit()

        # retorna o usuário criado
        return usuario

    def buscar_usuario_por_nome_usuario(self, nome_usuario:str):
        """
        Método que obtém um usuário pelo nome de usuário.
        :param nome_usuario: Nome de usuário do usuário.
        :return: Usuário encontrado (se existir) ou nulo
        caso contrário.
        """
        return self.__session.query(Usuario).filter_by(
            nome_usuario=nome_usuario).first()

    def atualizar_usuario(self, usuario:Usuario):
        """
        Método que atualiza um usuário.
        :param usuario: Usuário que será atualizado.
        """
        usuario.versao += 1
        usuario.data_atualizacao = datetime.now()
        self.__session.commit()
        return usuario

    def deletar_usuario(self, usuario:Usuario):
        """
        Método que deleta um usuário.
        :param usuario: Usuário que será deletado.
        """
        self.__session.delete(usuario)
        self.__session.commit()

    def listar_usuarios(self):
        """
        Método que lista todos os usuários.
        :return: Lista de usuários.
        """
        return self.__session.query(Usuario).all()