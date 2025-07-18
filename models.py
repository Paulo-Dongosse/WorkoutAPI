from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from dependencis import Base  # IMPORTA O BASE CORRETO DO SEU ARQUIVO DE DEPENDENCIAS

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)

    atletas = relationship("Atleta", back_populates="categoria")
    
    


class CentroTreinamento(Base):
    __tablename__= "centros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    endereco = Column(String)

    atletas = relationship("Atleta", back_populates="centro_treinamento")

    



class Atleta(Base):
    __tablename__ = "atletas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    idade = Column(Integer)
    peso = Column(Float)
    altura = Column(Float)
    sexo = Column(String(1))  # "M" ou "F"

    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    centro_treinamento_id = Column(Integer, ForeignKey("centros.id"))

    categoria = relationship("Categoria", back_populates="atletas")
    centro_treinamento = relationship("CentroTreinamento", back_populates="atletas")

    