from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Atleta
from schemas import AtletaSchema, AtletaOut
from dependencis import get_db
from typing import List

atleta_router = APIRouter(prefix="/atletas", tags=["atletas"])

@atleta_router.post("/criar-atleta", response_model=AtletaOut)
def criar_novo_atleta(atleta: AtletaSchema, session: Session = Depends(get_db)):
    """
        para criar Atleta é preciso seguir o Schema abaixo     
    """
    atleta_existente = session.query(Atleta).filter(Atleta.cpf == atleta.cpf).first()
    if atleta_existente:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    
    novo_atleta = Atleta(**atleta.dict())
    session.add(novo_atleta)
    session.commit()
    session.refresh(novo_atleta)
    return novo_atleta


@atleta_router.get("/", response_model=List[AtletaSchema])
def consultar_atletas(session: Session = Depends(get_db)):
    atletas = session.query(Atleta).all()
    return atletas

@atleta_router.get("/{atleta_id}", response_model=AtletaSchema)
def consultar_atleta_Pelo_id(atleta_id: int, session: Session = Depends(get_db)):
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return atleta

@atleta_router.patch("/{atleta_id}", response_model=AtletaSchema)
def editar_atleta_pelo_id(atleta_id: int, dados: AtletaOut, session: Session = Depends(get_db)):
    """
        para Editar Atleta é preciso seguir o Schema abaixo, preenchendo todos os campos    
    """
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    for chave, valor in dados.dict(exclude_unset=True).items():
        setattr(atleta, chave, valor)
    session.commit()
    session.refresh(atleta)
    return atleta

@atleta_router.delete("/{atleta_id}", status_code=status.HTTP_200_OK)
def deletar_atleta_pelo_id(atleta_id: int, session: Session = Depends(get_db)):
    atleta = session.query(Atleta).filter(Atleta.id == atleta_id).first()
    if not atleta:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    session.delete(atleta)
    session.commit()
    return {"msg": f"{atleta.nome} Atleta excluído com sucesso"}
