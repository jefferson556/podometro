import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Float
Base = declarative_base()

class Samples(Base):
    __tablename__ = 'muestras'
    id=Column(Integer, primary_key=True)
    pasos=Column('pasos', Integer)
    distancia=Column('distancia', Float)
    calorias=Column('calorias', Float)
    velocidad=Column('velocidad', Float)

    def serialize(self):
    	return{
    		'id' : self.id,
    		'pasos' : self.pasos,
    		'distancia' : self.distancia,
    		'calorias' : self.calorias,
    		'velocidad' : self.velocidad
    	}