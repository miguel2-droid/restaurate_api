from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Cliente_data(Base):
    __tablename__ = "Clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    status_id = Column(Integer, ForeignKey("status.id"), nullable=False)

    status = relationship("Status_data")

class Status_data(Base):
    __tablename__= "Status"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)

class Pratos_data(Base):
    __tablename__ ="Pratos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String,index=True)
    preco = Column(String, index=True)
    categoria_id = Column(Integer, primary_key=True, index=True )

