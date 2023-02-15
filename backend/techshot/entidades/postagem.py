from pydantic import BaseModel


class PostagemCriacao (BaseModel):
    """
    Classe que representa uma postagem de um usuário da rede social Piui.
    """
    texto: str