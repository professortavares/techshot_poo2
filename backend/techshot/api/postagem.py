from techshot.entidades import PostagemCriacao
from techshot.servicos.postagem import ServicoPostagem
from techshot.orm.database import get_session
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends

# cria uma instância de FastAPI para o módulo de usuários
router = APIRouter()

class PostagemAPI:

    """
    Classe que representa a API de usuários
    """
    @staticmethod
    @router.post("/postagens")
    def criar_postagem(postagem:PostagemCriacao,
                       nome_usuario:str,
                      session: Session = Depends(get_session)):
        """
        Método responsável por criar uma nova postagem

        --- Parâmetros ---
        :param dados_usuario:
        :param session:

        --- Retorno ---
        :return:

        """
        servico = ServicoPostagem(session)
        postagem = servico.criar_postagem(postagem, nome_usuario)
        return postagem

    @staticmethod
    @router.get("/postagens")
    def buscar_todas_postagem(session: Session = Depends(get_session)):
        servico = ServicoPostagem(session)
        try:
            postagem = servico.buscar_todas_postagem()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=str(e))
        return postagem

    @staticmethod
    @router.get("/postagens/{nome_usuario}")
    def buscar_postagem_por_nome_usuario(nome_usuario:str,
                                         session: Session = Depends(get_session)):
        servico = ServicoPostagem(session)
        try:
            postagens = servico.buscar_postagem_por_nome_usuario(nome_usuario)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=str(e))
        return postagens

