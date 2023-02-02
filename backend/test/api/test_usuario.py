import pytest
from pytest import fixture
from techshot.api import ApiUsuario
from fastapi.testclient import TestClient
from techshot.orm.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from techshot.orm.database import get_session

# cria uma instância de engine
engine = create_engine('sqlite:///:memory:', echo=True)
# cria as tabelas necessárias
Base.metadata.create_all(bind=engine)
# cria uma instância de sessionmaker
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session_new():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@fixture(scope='module')
def client():
    app = FastAPI()
    api_usuario = ApiUsuario()
    app.include_router(api_usuario.router)
    app.dependency_overrides[get_session] = get_session_new
    return TestClient(app)

def test_crud_usuario_api(client):
    #add
    response = client.post('/usuarios', json={"nome": "Joao", 
                                   "nome_usuario": "jao"})
    assert response.status_code == 200
    #search not found
    response = client.get('/usuarios/xxxx')
    assert response.status_code == 404
    assert response.json() == { 
        "detail": "Usuário não encontrado" }
    #search found
    response = client.get('/usuarios/jao')
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['nome'] == "Joao"
    assert response_data['nome_usuario'] == 'jao'
    assert response_data['versao'] == 1


    


