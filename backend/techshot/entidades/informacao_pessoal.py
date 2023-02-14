from datetime import datetime
from pydantic import BaseModel, ValidationError, validator
from techshot.aux_function import codifica_senha

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
        # encripta a senha
        
        return codifica_senha(senha)
    
    @validator('data_nascimento')
    def validar_idade(cls, data_nascimento):
        idade = datetime.now().year - data_nascimento.year - 1
        if datetime.now().month > data_nascimento.month or ( \
             datetime.now().month == data_nascimento.month and \
             datetime.now().day >= data_nascimento.day):
            idade += 1
        if idade < 12:
            raise ValidationError('O usuário deve ter pelo menos 12 anos.')
        return data_nascimento
