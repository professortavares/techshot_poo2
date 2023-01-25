from datetime import datetime
from pydantic import BaseModel, ValidationError, validator

class InformacaoPessoalCriacao(BaseModel):
    """
    Classe que representa as informações pessoais de um
    usuário da rede social Piui.
    """
    email: str
    telefone: str
    senha: str
    data_nascimento: datetime

    @validator('senha')
    def validar_senha(cls, senha):
        # Valida se a senha possui no mínimo 6 caracteres.
        if len(senha) < 6:
            raise ValidationError('A senha deve ter pelo menos 6 caracteres.')
        return senha