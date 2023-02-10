from pydantic import BaseModel, ValidationError, validator

class UsuarioCriacao(BaseModel):
    """
    Classe que representa um usuário da rede
    social Piui.
    """
    nome: str
    nome_usuario: str

    @validator('nome')
    def nome_maior_que_3(cls, nome):
        if len(nome) < 3:
            raise ValidationError('O nome deve ter mais de 3 caracteres.')
        elif len(nome) > 50:
            raise ValidationError('O nome deve ter menos de 50 caracteres.')
        return nome

