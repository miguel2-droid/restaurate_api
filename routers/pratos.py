from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter(prefix="/pratos", tags=["Pratos"])

@router.post("/", response_model=schemas.Prato)
def criar(pratos: schemas.Prato, db:Session = Depends(database.get_db)):
    return crud.criar_prato(db, pratos)

@router.get("/", response_model=schemas.Prato)
def listar(pratos: schemas.Prato, db:Session = Depends(database.get_db)):
    return crud.listar_pratos(db)

@router.get("/{buscar}", response_model=schemas.Prato)
def buscar(nome: str, db: Session = Depends(database.get_db)):
    return crud.buscar_prato_pelo_nome

@router.get("/{id}", response_model=schemas.Prato)
def obter(pratos: schemas.Prato, db:Session = Depends(database.get_db)):
    return crud.buscar_prato_id(db, id)

@router.put("/", response_model=schemas.Prato)
def alterar(pratos: schemas.Prato, db:Session = Depends(database.get_db)):
    return crud.alterar_prato