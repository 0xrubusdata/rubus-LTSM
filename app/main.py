from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from app.config.settings import DATABASE_URL
from app.routes.data import router as data_router
from app.routes.model import router as model_router
from app.routes.config import router as config_router
from app.routes.plot import router as plot_router

engine = create_engine(DATABASE_URL)
app = FastAPI(
    title="Rubus LSTM API",
    description="API for stock price prediction using LSTM.",
    version="0.1.0"
)

def get_session():
    with Session(engine) as session:
        yield session

app.include_router(data_router, prefix="/data")
app.include_router(model_router, prefix="/model")
app.include_router(config_router, prefix="/config")
app.include_router(plot_router, prefix="/plot")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)