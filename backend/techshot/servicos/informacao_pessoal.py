from datetime import datetime

from techshot.entidades.informacao_pessoal import InformacaoPessoalCriacao
from techshot.orm.informacao_pessoal import InformacaoPessoal
from techshot.orm.usuario import Usuario
class ServicoInformacaoPessoal:

    def __init__(self, session):
        """
        Construtor da classe.
        :param session:
        """
        self.__session = session

    def criar_informacao_pessoal(self,
                                 dados_informacao_pessoal:InformacaoPessoalCriacao):
        """
        Método que cria uma nova informação pessoal, vincula
        ao usuário e salva no banco de dados.
        :param usuario: Usuário que será vinculado à informação pessoal.
        :param dados_informacao_pessoal: Dados da informação pessoal.
        :return: Informação pessoal criada.
        """
        # cria uma instância de informação pessoal
        informacao_pessoal = InformacaoPessoal(**dados_informacao_pessoal.dict())

        # salva a informação pessoal no banco de dados
        self.__session.add(informacao_pessoal)
        # salva as alterações no banco de dados
        self.__session.commit()
        # retorna a informação pessoal criada
        return informacao_pessoal

    def buscar_informacao_pessoal_por_usuario(self, usuario:Usuario):
        """
        Método que obtém a informação pessoal de um usuário.
        :param usuario: Usuário que será vinculado à informação pessoal.
        :return: Informação pessoal do usuário (se existir) ou nulo
        caso contrário.
        """
        return self.__session.query(InformacaoPessoal).filter_by(
            usuario=usuario).first()

    def atualizar_informacao_pessoal(self, informacao_pessoal:InformacaoPessoal):
        """
        Método que atualiza uma informação pessoal.
        :param informacao_pessoal: Informação pessoal que será atualizada.
        """
        informacao_pessoal.versao += 1
        informacao_pessoal.data_atualizacao = datetime.now()

        self.__session.commit()
        return informacao_pessoal

    def deletar_informacao_pessoal(self, informacao_pessoal:InformacaoPessoal):
        """
        Método que deleta uma informação pessoal.
        :param informacao_pessoal: Informação pessoal que será deletada.
        """
        self.__session.delete(informacao_pessoal)
        self.__session.commit()

