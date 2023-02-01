import pytest
from pytest import fixture
from techshot.api import ApiUsuario
from fastapi.testclient import TestClient
from techshot.orm.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

@fixture(scope='module')
def session():
    # cria uma instância de engine
    engine = create_engine('sqlite:///:memory:', echo=True)
    # cria as tabelas necessárias
    Base.metadata.create_all(bind=engine)

    # cria uma instância de sessionmaker
    Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    # cria uma instância de sessão
    session = Session()
    return session