from sqlalchemy import create_engine, Column, Integer, String
from techshot.orm.base import Base
from sqlalchemy.orm import sessionmaker

# Cria uma instância de engine
engine = create_engine('sqlite:///volume/techshot.db', echo=True)

# Cria uma instância de sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base de dados
Base.metadata.create_all(engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()