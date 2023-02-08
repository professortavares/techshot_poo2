

class ApiBase:
    """
    Classe base para as APIs
    """

    @staticmethod
    def get_session_base():
        """
        Método responsável por retornar uma instância de sessão do banco de dados
        :return:
        """
        return get_session()