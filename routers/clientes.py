from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter(prefix="/cliente", tags=["Clientes"])


@router.post("/", response_model=schemas.Cliente)
def criar(cliente: schemas.Cliente, db:Session = Depends(database.get_db)):
    return crud.criar_cliente(db, cliente)

@router.get("/listar/", response_model=schemas.Cliente)
def listar(cliente: schemas.Cliente, db:Session = Depends(database.get_db)):
    return crud.listar_cliente(db)

@router.get("/buscar")
def buscar(nome: str, db:Session = Depends(database.get_db)):
    return crud.obter_cliente_por_nome(db, nome)

@router.get("/{id}", response_model=schemas.Cliente)
def obter(id: int, db:Session = Depends(database.get_db)):
    return crud.buscar_cliente_pelo_id(db, id)

@router.put("/", response_model=schemas.Cliente)
def alternar(cliente: schemas.Cliente, db:Session = Depends(database.get_db)):
    return crud.criar_cliente(db, id, cliente)

@router.delete("/", response_model=schemas.Cliente)
def deletar(cliente: schemas.Cliente, db:Session = Depends(database.get_db)):
    return crud.criar_cliente(db, id)
