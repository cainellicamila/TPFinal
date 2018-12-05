from sqlalchemy import Column, Integer, String, create_engine, func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime


Base = declarative_base()


class Consulta(Base):
    __tablename__ = 'consultas'

    id_consulta=  Column(Integer,primary_key=True, autoincrement=True)
    direccion = Column(String(100), nullable=False)
    eleccion = Column(String(50), nullable=False)
    hora = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

