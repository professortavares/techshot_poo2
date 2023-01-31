from techshot.entidades import UsuarioCriacao
from techshot.servicos.servico_usuario import ServicoUsuario
from fastapi import status, HTTPException, Depends
from techshot.orm.database import get_session
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter

# cria uma instância de FastAPI para o módulo de usuários
router = APIRouter()

@router.post("/usuarios")
def criar_usuario(dados_usuario:UsuarioCriacao,
                  session: Session = Depends(get_session)):
    """
    Método responsável por criar um novo usuário
    :param dados_usuario:
    :param session:
    :return:
    """
    servico = ServicoUsuario(session)
    return servico.criar_usuario(dados_usuario)

@router.get("/usuarios/{nome_usuario}")
def buscar_usuario_por_nome_usuario(nome_usuario:str,
                                    session: Session = Depends(get_session)):
    """
    Método responsável por buscar um usuário pelo nome de usuário
    :param nome_usuario: nome de usuário
    :param session:
    :return: Usuário encontrado (se existir) ou nulo caso contrário.
    """
    servico = ServicoUsuario(session)
    usuario = servico.buscar_usuario_por_nome_usuario(nome_usuario)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuário não encontrado")
    return usuario

@router.put("/usuarios/{nome_usuario}")
def atualizar_usuario(nome_usuario:str,
                        dados_usuario:UsuarioCriacao,
                        session: Session = Depends(get_session)):
        """
        Método responsável por atualizar um usuário
        :param nome_usuario: nome de usuário
        :param dados_usuario: dados do usuário
        :param session:
        :return: Usuário atualizado
        """
        servico = ServicoUsuario(session)
        usuario = servico.buscar_usuario_por_nome_usuario(nome_usuario)
        if usuario is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Usuário não encontrado")

        # Atualiza os dados do usuário
        usuario.nome = dados_usuario.nome

        return servico.atualizar_usuario(usuario)

@router.delete("/usuarios/{nome_usuario}")
def deletar_usuario(nome_usuario:str,
                    session: Session = Depends(get_session)):
    """
    Método responsável por deletar um usuário
    :param nome_usuario: nome de usuário
    :param session:
    :return: Usuário deletado
    """
    servico = ServicoUsuario(session)
    usuario = servico.buscar_usuario_por_nome_usuario(nome_usuario)
    servico.deletar_usuario(usuario)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Usuário não encontrado")

    return None

@router.get("/usuarios")
def listar_usuarios(session: Session = Depends(get_session)):
    """
    Método responsável por listar todos os usuários
    :param session:
    :return: Lista de usuários
    """
    servico = ServicoUsuario(session)
    return servico.listar_usuarios()
