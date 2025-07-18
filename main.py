from fastapi import FastAPI
from models import Base
from dependencis import engine
from atleta_routes import atleta_router
from centro_routes import centro_router
from categoria_routes import categoria_router
from fastapi_pagination import add_pagination


app = FastAPI(title="workoutAPI")
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

#uvicorn main:app --reload
# pra colocar-lo no ar

app.include_router(atleta_router)
app.include_router(categoria_router)
app.include_router(centro_router)


add_pagination(app)