from sqlalchemy import create_engine
from techshot.orm.usuario import Usuario
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from techshot.orm.database import get_session
from techshot.api.usuario import UsuarioApi
from fastapi.testclient import TestClient
from pytest import fixture


@fixture
def criar_client():
    # cria uma instância de engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    # cria as tabelas necessárias
    Usuario.metadata.create_all(bind=engine)
    # cria uma instância de sessionmaker
    session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    def new_get_session():
        db = session()
        try:
            yield db
        finally:
            db.close()

    app = FastAPI()
    api_usuario = UsuarioApi()
    app.include_router(api_usuario.router)
    app.dependency_overrides[get_session] = new_get_session
    return TestClient(app)


def test_criar_usuario(criar_client):
    resposta = criar_client.post('/usuarios', json={"nome": "Arthur",
                                              "nome_usuario": "tutu"})
    assert resposta.status_code == 200


def test_buscar_usuario(criar_client):
    resposta = criar_client.get('/usuarios/123')
    resposta1 = criar_client.get('/usuarios/tutu')
    resposta_data = resposta1.json()
    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "Usuário não encontrado"}
    assert resposta1.status_code == 200
    assert resposta_data['nome'] == "Arthur"
    assert resposta_data['nome_usuario'] == 'tutu'
    assert resposta_data['versao'] == 1

def test_atualizar_usuario(criar_client):
    resposta = criar_client.get('/usuarios/123')
    resposta1 = criar_client.put('usuarios/tutu', json={"nome": "Eduardo",
                                              "nome_usuario": "tutu"})
    resposta_data = resposta1.json()
    assert resposta_data['nome'] == 'Eduardo'
    assert resposta_data['nome_usuario'] == 'tutu'
    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "Usuário não encontrado"}


def test_deletar_usuario(criar_client):
    resposta = criar_client.get('/usuarios/123')
    resposta1 = criar_client.post('/usuarios', json={"nome": "Matilde",
                                                    "nome_usuario": "doidinha"})
    resposta1 = criar_client.delete('usuarios/doidinha', json={"nome": "Matilde","nome_usuario": "doidinha"})
    resposta_data = resposta1.json()
    assert resposta_data['nome_usuario'] == []
    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "Usuário não encontrado"}


def test_listar_usuario(criar_client):
    resposta = criar_client.post('/usuarios', json={"nome": "Arthur",
                                                    "nome_usuario": "tutu"})
    resposta = criar_client.post('/usuarios', json={"nome": "Matilde",
                                                     "nome_usuario": "doidinha"})
    resposta = criar_client.get('/usuarios')
    resposta_data = resposta.json()
    assert resposta.status_code == 200
    assert resposta_data[0]['nome_usuario'] == "tutu"
    assert resposta_data[1]['nome_usuario'] == "doidinha"