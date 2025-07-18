from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate

import models, schemas
from dependencis import get_db, Base


categoria_router = APIRouter(prefix="/categorias", tags=["Categorias"])

@categoria_router.post("/", response_model=schemas.CategoriaOut, status_code=status.HTTP_201_CREATED)
def criar_Uma_categoria(categoria: schemas.CategoriaSchema, session: Session = Depends(get_db)):
    db_categoria = models.Categoria(**categoria.dict())
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return db_categoria

@categoria_router.get("/", response_model=Page[schemas.CategoriaOut])
def Consultar_categorias(session: Session = Depends(get_db)):
    categorias = session.query(models.Categoria).all()
    return paginate(categorias)

@categoria_router.get("/{categoria_id}", response_model=schemas.CategoriaOut)
def consultar_categoria_pelo_id(categoria_id: int, session: Session = Depends(get_db)):
    categoria = session.query(models.Categoria).get(categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria


