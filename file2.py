from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Volume(Base):
    __tablename__ = "volumes"
    id = Column(Integer, primary_key=True)
    date = Column(String)
    volume = Column(Float)