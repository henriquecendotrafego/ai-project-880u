from fastapi import FastAPI, Response
from pydantic import BaseModel
from yfinance import Ticker
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Configuração do banco de dados
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db_name"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Volume(Base):
    __tablename__ = "volumes"
    id = Column(Integer, primary_key=True)
    date = Column(String)
    volume = Column(Float)

Base.metadata.create_all(engine)

@app.get("/volumes")
def get_volumes():
    with SessionLocal() as session:
        volumes = session.query(Volume).all()
        return {"volumes": [volume.__dict__ for volume in volumes]}

@app.get("/volumes/{date}")
def get_volume_by_date(date: str):
    with SessionLocal() as session:
        volume = session.query(Volume).filter(Volume.date == date).first()
        if volume:
            return {"volume": volume.__dict__}
        else:
            return {"error": "Volume not found for the given date"}

@app.post("/volumes")
def create_volume(volume: dict):
    with SessionLocal() as session:
        new_volume = Volume(**volume)
        session.add(new_volume)
        session.commit()
        return {"message": "Volume created successfully"}