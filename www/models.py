import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Float
Base = declarative_base()

class Muestras(Base):
    __tablename__ = 'muestras'
    id=Column(Integer, primary_key=True)
    pasos=Column('pasos', Integer)
    distancia=Column('distancia', Float)
    calorias=Column('calorias', Float)
    velocidad=Column('velocidad', Float)
    
    def __init__(self,pasos,distancia,calorias,velocidad):
        self.pasos=pasos
        self.distancia=distancia
        self.calorias=calorias
        self.velocidad=velocidad

   