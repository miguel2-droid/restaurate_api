from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    nome: str
    telefone: str
    class Config:
        orm_mode = True

class Status_Cliente(BaseModel):
    id: int
    descricao: str

    class Config:
        orm_mode = True

class Prato(BaseModel):
    id: int
    nome: str
    preco: str
    categoria_id: int