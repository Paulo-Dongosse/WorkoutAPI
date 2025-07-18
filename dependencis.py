from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from settings import DATABASE_URL

Base = declarative_base()

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # obrigatório para SQLite + FastAPI
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
