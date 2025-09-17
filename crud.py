from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas

def criar_cliente(db:Session, cliente: schemas.Cliente):
        cliente_data = models.Cliente_data(nome = cliente.nome, telefone = cliente.telefone)
        

        db.add(cliente_data)
        db.commit()
        db.refresh(cliente_data)
        db.close()

        return cliente_data

def buscar_cliente_pelo_id(db: Session, id: int ):
        clientes = db.query(models.Cliente_data).filter(models.Cliente_data.id == id).first()

        if not clientes:
            raise HTTPException(status_code=404, detail="Registro de cliente não encontrado")
    
        return clientes

def listar_cliente(db: Session):
    return db.query(models.Cliente_data).all()

def obter_cliente_por_nome(db: Session, nome: str):
      return db.query(models.Cliente_data).filter(models.Cliente_data.nome.ilike(f"%{nome}%")).all()
      
def alterar_cliente(db: Session, id: int, cliente: schemas.Cliente ):
        clientes_data = db.query(models.Cliente_data).filter(models.Cliente_data.id == id).first()

        if not clientes_data:
            raise HTTPException(status_code=404, detail= "Erro ao alterar registro de cliente")
   
        clientes_data.nome = cliente.nome

        db.commit()
        db.refresh(clientes_data)

        return clientes_data
    
def deletar_cliente(db: Session, id: int):
        clientes_data = db.query(models.Cliente_data).filter(models.Cliente_data.id == id).first()

        if not clientes_data:
            raise HTTPException(status_code=404, detail="Erro ao deletar registro cliente")
        
       

        db.delete(clientes_data)
        db.commit()
        

        return ("mensagem: Cliente excluido com sucesso")

def criar_status(db: Session):
    status_padrao = ["Ativo", "Inativo"]
    for descricao in status_padrao:
        db.add(models.Status_cliente_data(descricao=descricao))
    db.commit()
    return {"Mensagem": "Status de cliente criado!"}

def criar_prato(db:Session, prato: schemas.Prato):
        pratos_data = models.Pratos_data(nome = prato.nome, preco = prato.preco)

        db.add(pratos_data)
        db.commit()
        db.refresh(pratos_data)
        db.close()

      
        return pratos_data

def buscar_prato_id(db:Session, id: int):
      pratos = db.query(models.Pratos_data).filter(models.Pratos_data.id == id)
      if not pratos:
            raise HTTPException(status_code=404, detail="Erro ao identificar pedido do cliente")
      
      return pratos

def listar_pratos(db:Session):
      pratos_data = db.query(models.Pratos_data).filter(models.Pratos_data.id == id)
      return db.query(models.Pratos_data).all()
      

def buscar_prato_pelo_nome(db: Session, nome: str):
      return db.query(models.Pratos_data).filter(models.Pratos_data.nome.ilike(f"%{nome}%")).all()

def alterar_prato(db: Session, id:int, pratos:schemas.Prato):
      pratos_data = db.query(models.Pratos_data).filter(models.Pratos_data.id == id)
      if not pratos_data:
            raise HTTPException(status_code=404, detail= "Erro ao alterar registro de prato")
      
      return pratos_data




      

