from datetime import datetime

from techshot.entidades.informacao_pessoal import InformacaoPessoalCriacao
from techshot.orm.informacao_pessoal import InformacaoPessoal
from techshot.orm.usuario import Usuario
from techshot.aux_function import codifica_senha

class ServicoInformacaoPessoal:

    def __init__(self, session):
        """
        Construtor da classe.
        :param session: Sessão do banco de dados.
        """
        self.__session = session

    def criar_informacao_pessoal(self, dados_informacao: InformacaoPessoalCriacao):
        """
        Método que cria um novo usuário e
        salvá-lo no banco de dados.
        :param dados_informacao: Dados da informacao pessoal que será criada.
        :return: informacaopessoal criada.
        """

        # cria uma instância de usuário
        info_pessoal = InformacaoPessoal(**dados_informacao.dict())
        info_pessoal.versao = 1
        info_pessoal.data_criacao = datetime.now()
        info_pessoal.data_atualizacao = datetime.now()
        
        # salva o usuário no banco de dados
        self.__session.add(info_pessoal)
        # salva as alterações no banco de dados
        self.__session.commit()

        # retorna o usuário criado
        return info_pessoal

    def buscar_informacao_pessoal_por_usuario(self, usuario:Usuario):
        """
        Método que obtém uma informação pessoal pelo id do usuário.
        :param id_usuario: id do usuário do usuário.
        :return: Usuário encontrado (se existir) ou nulo
        caso contrário.
        """
        return self.__session.query(InformacaoPessoal).filter_by(
            usuario=usuario).first()

    def atualizar_informacao_pessoal(self, informacao_pessoal: InformacaoPessoal):
        """
        Método que atualiza as informações de usuario.
        :param informacao_pessoal: InformaçãoPessoal que será atualizada.
        """
        informacao_pessoal.versao += 1
        informacao_pessoal.data_atualizacao = datetime.now()
        informacao_pessoal.senha = codifica_senha(informacao_pessoal.senha)

        self.__session.commit()
        return informacao_pessoal

    def deletar_informacao_pessoal(self, informacao_pessoal: InformacaoPessoal):
        """
        Método que deleta informacao pessoal.
        :param usuario: Usuário que será deletado.
        """
        self.__session.delete(informacao_pessoal)
        self.__session.commit()