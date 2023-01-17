class Usuario:
    """
    Classe que representa um usuário da rede
    social Piui.
    """

    def __init__(self,
                 nome:str,
                 nome_usuario:str):
        """
        Construtor da classe.

        :param nome: Nome completo do usuário.
        :param nome_usuario: Nome de usuário da rede social (@).
        """
        self.nome = nome
        self.nome_usuario = nome_usuario
        # As informações abaixo serão adicionadas posteriormente.
        self.informacoes_pessoais = None
        self.postagens = []

