from techshot.entidades import UsuarioCriacao
from techshot.servicos.usuario import ServicoUsuario
from techshot.orm.database import get_session
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter
from fastapi import status, HTTPException, Depends
from techshot.servicos.servico_informacaopessoal import ServicoInformacaoPessoal
from techshot.entidades import InformacaoPessoalCriacao

class ApiUsuario:

    def __init__(self):
        # cria uma instância de FastAPI para o módulo de usuários
        self.router = APIRouter()
        self.router.add_api_route("/usuarios", self.criar_usuario, methods=['POST'])
        self.router.add_api_route("/usuarios", self.listar_usuarios, methods=['GET'])
        self.router.add_api_route("/usuarios/{nome_usuario}", self.buscar_usuario_por_nome_usuario, methods=['GET'])
        self.router.add_api_route("/usuarios/{nome_usuario}", self.atualizar_usuario, methods=['PUT'])
        self.router.add_api_route("/usuarios/{nome_usuario}", self.deletar_usuario, methods=['DELETE'])
        self.router.add_api_route("/info_pessoal/{nome_usuario}", self.criar_informacao_pessoal, methods=["POST"])
        self.router.add_api_route("/info_pessoal/{nome_usuario}", self.buscar_informacao_pessoal_por_nome_usuario, methods=['GET'])
        self.router.add_api_route("/info_pessoal/{nome_usuario}", self.atualizar_informacao_pessoal, methods=['PUT'])
        self.router.add_api_route("/info_pessoal/{nome_usuario}", self.deletar_informacao_pessoal, methods=['DELETE'])

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
        if usuario is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Usuário não encontrado")
        servico.deletar_usuario(usuario)
        return None


    def listar_usuarios(self, session: Session = Depends(get_session)):
        """
        Método responsável por listar todos os usuários
        :param session:
        :return: Lista de usuários
        """
        servico = ServicoUsuario(session)
        return servico.listar_usuarios()

    def criar_informacao_pessoal(self, nome_usuario: str, dado_info_pessoal:InformacaoPessoalCriacao,
                                 session: Session = Depends(get_session)):
        """
        Método responsável por criar informações pessoais de um usuário
        :param nome_usuario:
        :param dado_info_pessoal:
        :param session:
        :return:
        """
        usuario = ServicoUsuario(session).buscar_usuario_por_nome_usuario(nome_usuario)
        servico = ServicoInformacaoPessoal(session)
        info = servico.criar_informacao_pessoal(dado_info_pessoal)
        usuario.informacao_pessoal = info
        session.commit()
        return info

    def buscar_informacao_pessoal_por_nome_usuario(self, nome_usuario:str,
                                        session: Session = Depends(get_session)):
        """
        Método responsável por buscar um usuário pelo nome de usuário
        :param nome_usuario: nome de usuário
        :param session:
        :return: Informação Pessoal encontrado (se existir) ou nulo caso contrário.
        """
        usuario = ServicoUsuario(session).buscar_usuario_por_nome_usuario(nome_usuario)
        servico = ServicoInformacaoPessoal(session)
        info_pessoal = servico.buscar_informacao_pessoal_por_usuario(usuario)
        if info_pessoal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Usuário não encontrado")
        return info_pessoal

    def atualizar_informacao_pessoal(self, nome_usuario:str,
                            nova_info_pessoal:InformacaoPessoalCriacao,
                            session: Session = Depends(get_session)):
            """
            Método responsável por atualizar um usuário
            :param nome_usuario: nome de usuário
            :param info_pessoal: dados da informação pessoal
            :param session:
            :return: informação pessoal atualizada
            """
            usuario = ServicoUsuario(session).buscar_usuario_por_nome_usuario(nome_usuario)
            servico = ServicoInformacaoPessoal(session)
            info_pessoal = servico.buscar_informacao_pessoal_por_usuario(usuario)
            if info_pessoal is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Usuário não encontrado")
            info_pessoal.email = nova_info_pessoal.email
            info_pessoal.telefone = nova_info_pessoal.telefone
            info_pessoal.senha = nova_info_pessoal.senha
            info_pessoal.data_nascimento = nova_info_pessoal.data_nascimento
            # info_pessoal.__dict__.update(nova_info_pessoal.__dict__)
            # Atualiza os dados do info_pessoal
            
            return servico.atualizar_informacao_pessoal(info_pessoal)
    
    def deletar_informacao_pessoal(self, nome_usuario:str,
                        session: Session = Depends(get_session)):
        """
        Método responsável por deletar um usuário
        :param nome_usuario: nome de usuário
        :param session:
        :return: Usuário deletado
        """
        usuario = ServicoUsuario(session).buscar_usuario_por_nome_usuario(nome_usuario)
        if usuario is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Informação pessoal não encontrada")
        servico = ServicoInformacaoPessoal(session)
        servico.deletar_informacao_pessoal(usuario)
        return None
