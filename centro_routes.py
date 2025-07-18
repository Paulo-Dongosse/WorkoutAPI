from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi_pagination import Page, paginate

import models, schemas
from dependencis import get_db, Base


centro_router = APIRouter(prefix="/centros", tags=["Centros de Treinamento"])

@centro_router.post("/", response_model=schemas.CentroTreinamentoOut, status_code=status.HTTP_201_CREATED)
def criar_centro_de_Treinamento(centro: schemas.CentroTreinamentoSchema, session: Session = Depends(get_db)):
    db_centro = models.CentroTreinamento(**centro.dict())
    session.add(db_centro)
    session.commit()
    session.refresh(db_centro)
    return db_centro

@centro_router.get("/", response_model=Page[schemas.CentroTreinamentoOut])
def consultar_centro_de_treinamento(session: Session = Depends(get_db)):
    centros = session.query(models.CentroTreinamento).all()
    return paginate(centros)

@centro_router.get("/{centro_id}", response_model=schemas.CentroTreinamentoOut)
def consultar_centro_pelo_id(centro_id: int, session: Session = Depends(get_db)):
    centro = session.query(models.CentroTreinamento).get(centro_id)
    if not centro:
        raise HTTPException(status_code=404, detail="Centro não encontrado")
    return centro

