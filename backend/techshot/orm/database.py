from sqlalchemy import create_engine, Column, Integer, String
from techshot.orm.usuario import Usuario
from sqlalchemy.orm import sessionmaker

# Cria uma instância de engine
engine = create_engine('sqlite:///techshot.db', echo=True)

# Cria uma instância de sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a base de dados
Usuario.metadata.create_all(engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()