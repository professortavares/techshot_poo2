from techshot.entidades import UsuarioCriacao
from techshot.servicos.usuario import ServicoUsuario
from techshot.orm.database import get_session
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends


class ApiUsuario:

    def __init__(self):
        # cria uma instância de FastAPI para o módulo de usuários
        self.router = APIRouter()
        self.router.add_api_route("/usuarios", self.criar_usuario, methods=['POST'])
        self.router.add_api_route("/usuarios", self.listar_usuarios, methods=['GET'])
        self.router.add_api_route("/usuarios/{nome_usuario}", self.buscar_usuario_por_nome_usuario, methods=['GET'])
        self.router.add_api_route("/usuarios/{nome_usuario}", self.atualizar_usuario, methods=['PUT'])
        self.router.add_api_route("/usuarios/{nome_usuario}", self.deletar_usuario, methods=['DELETE'])

    def criar_usuario(self, dados_usuario:UsuarioCriacao,
                    session: Session = Depends(get_session)):
        """
        Método responsável por criar um novo usuário
        :param dados_usuario:
        :param session:
        :return:
        """
        servico = ServicoUsuario(session)
        return servico.criar_usuario(dados_usuario)

    def buscar_usuario_por_nome_usuario(self, nome_usuario:str,
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

    def atualizar_usuario(self, nome_usuario:str,
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

    def deletar_usuario(self, nome_usuario:str,
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


    def listar_usuarios(self, session: Session = Depends(get_session)):
        """
        Método responsável por listar todos os usuários
        :param session:
        :return: Lista de usuários
        """
        servico = ServicoUsuario(session)
        return servico.listar_usuarios()
