import pytest
from pytest import fixture
from techshot.api import ApiUsuario
from fastapi.testclient import TestClient
from techshot.orm.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from techshot.orm.database import get_session
from datetime import datetime, timedelta, date
from techshot.aux_function import codifica_senha


@fixture
def client():
    # cria uma instância de engine
    engine = create_engine('sqlite:///temp.db', echo=True)
    # cria as tabelas necessárias
    Base.metadata.create_all(bind=engine)
    # cria uma instância de sessionmaker
    session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    def get_session_new():
        db = session()
        try:
            yield db
        finally:
            db.close()
        
    app = FastAPI()
    api_usuario = ApiUsuario()
    app.include_router(api_usuario.router)
    app.dependency_overrides[get_session] = get_session_new
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)


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
    #put
    response = client.put('/usuarios/jao', json={"nome": "João", 
                                                 "nome_usuario": "jao"})
    assert response.status_code == 200
    response = client.get('/usuarios/jao')
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['nome'] == "João"
    assert response_data['nome_usuario'] == 'jao'
    assert response_data['versao'] == 2
    #delete
    response = client.delete('/usuarios/jao')
    assert response.status_code == 200
    response = client.get('/usuarios/jao')
    assert response.status_code == 404

def test_info_pessoal_api(client):
    data_teste = (datetime.today() - timedelta(days=365 * 15))
    data_str = data_teste.isoformat()
    client.post('/usuarios', json={"nome": "Joao", 
                                   "nome_usuario": "jao"})
    response = client.post('info_pessoal/jao', json={'email':'a@a.com.br',\
                'telefone':'(11) 99999-9999',\
                'data_nascimento': data_str,\
                'senha':'123456'})
    assert response.status_code == 200
    #search found
    response = client.get('/info_pessoal/jao')
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['email'] == 'a@a.com.br'
    assert response_data['telefone'] == '(11) 99999-9999'
    assert response_data['senha'] == codifica_senha('123456')
    assert date.fromisoformat(response_data['data_nascimento']) == data_teste.date()
    #put
    response = client.put('info_pessoal/jao', json={'email':'b@a.com.br',\
                'telefone':'(11) 99999-9998',\
                'data_nascimento':data_teste.isoformat(),\
                'senha':'654321'})
    assert response.status_code == 200
    response = client.get('/info_pessoal/jao')
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['email'] == 'b@a.com.br'
    assert response_data['telefone'] == '(11) 99999-9998'
    assert response_data['senha'] == codifica_senha('654321')
    assert response_data['versao'] == 2
    #delete
    response = client.delete('/info_pessoal/jao')
    assert response.status_code == 200
    response = client.get('/info_pessoal/jao')
    assert response.status_code == 404