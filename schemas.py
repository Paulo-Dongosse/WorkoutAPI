from pydantic import BaseModel
from typing import Optional


class CategoriaSchema(BaseModel):
    nome: str


class CategoriaOut(CategoriaSchema):
    id: int

    class Config:
        from_attributes = True


class CentroTreinamentoSchema(BaseModel):
    nome: str
    endereco: str


class CentroTreinamentoOut(CentroTreinamentoSchema):
    id: int

    class Config:
        from_attributes = True


class AtletaSchema(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    categoria_id: int
    centro_treinamento_id: int


# Este é o que a API vai devolver com nomes legíveis:
class AtletaOut(BaseModel):
    id: int
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str

    categoria: Optional[CategoriaOut] = None
    centro_treinamento: Optional[CentroTreinamentoOut] = None

    class Config:
        from_attributes = True
