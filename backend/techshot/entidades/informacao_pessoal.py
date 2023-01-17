from datetime import datetime

class InformacaoPessoal:
    """
    Classe que representa as informações pessoais de um
    usuário da rede social Piui.
    """
    def __init__(self,
                email:str,
                telefone:str,
                senha:str,
                data_nascimento:datetime):
        """
        Construtor da classe.
        :param email: Email do usuário.
        :param telefone: Telefone do usuário.
        :param senha: Senha do usuário para usar a rede social.
        :param data_nascimento: data de nascimento do usuário.
        """
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.data_nascimento = data_nascimento
