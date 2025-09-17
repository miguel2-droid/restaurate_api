from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Minha_URL_DATABASE = "sqlite:///./restaurante.db"

engine = create_engine(Minha_URL_DATABASE)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:    
        yield db
    finally:
        db.close()