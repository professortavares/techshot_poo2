from pydantic import BaseModel, ValidationError, validator

class Usuario(BaseModel):
    """
    Classe que representa um usuário da rede
    social Piui.
    """
    nome: str
    nome_usuario: str
    informacoes_pessoais:type(None) = None
    postagens: list[type(None)] = []


    @validator('nome')
    def validar_nome(cls, nome):
        """
        Valida o nome do usuário: segundo a regra
        o nome de usuário deve ter no mínimo 3 caracteres.

        :param nome: Nome do usuário.
        :return: Nome do usuário.
        """
        if len(nome) < 3:
            raise ValueError('O nome do usuário deve ter pelo menos 3 caracteres.')
        return nome

